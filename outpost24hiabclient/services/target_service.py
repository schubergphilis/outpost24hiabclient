#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: targetstree_service.py

from requests import Session
import xml.etree.ElementTree as ET
import json
import multiprocessing
from joblib import Parallel, delayed

from ..tools import (xmltools, log)
from outpost24hiabclient.clients.hiabclient import HiabClient
from ..entities.targets_tree import TargetsTree, TargetGroupNode, TargetNode


class TargetService:

    def __init__(self, hiabclient):
        self._logger = log.getLogger(__name__)
        self._hiabclient = hiabclient

    def get_targets_tree(self):
        self.refresh()
        return self._targetgroups_tree

    def get_target_nodes(self):
        self.refresh()
        return self._targetgroups_tree.get_all_target_nodes()

    def get_targetgroup_nodes(self):
        self.refresh()
        return self._targetgroups_tree.get_all_targetgroup_nodes()

    def create_targetgroup_node_from_fq_string(self, fq):
        if(fq is None):
            return None
        if(fq == ""):
            return None

        targetgroupnamecomponents = fq.split('\\')

        self.refresh()
        targetgroup_node = self._targetgroups_tree.get_root_node()
        i=1
        while(i<len(targetgroupnamecomponents)-1):
            root_targetgroup_name = targetgroupnamecomponents[i]
    
            if(targetgroup_node.get_targetgroup().name == root_targetgroup_name):
                child_targetgroup_name = targetgroupnamecomponents[i+1]
                child = targetgroup_node.get_child_with_name(child_targetgroup_name)
                
                if(child is None):
                    # create child in op24
                    parent_targetgroup=targetgroup_node.get_targetgroup()
                    new_targetgroup = self._hiabclient.create_targetgroup(child_targetgroup_name, parent_targetgroup)
                    child = TargetGroupNode(new_targetgroup, targetgroup_node)
                    targetgroup_node.add_child(child)
                    

                targetgroup_node = child
            i = i+1

        return targetgroup_node

    def create_target_node(self, targetaddress, targetgroup_name, scanner_name, dnslookup):
        self.refresh()
        scanner = self.get_scanner_by_name(scanner_name)
        targetgroup_node = self._targetgroups_tree.get_targetgroup_node_from_fq_string(targetgroup_name)
        targetgroup = targetgroup_node.get_targetgroup()
        target = self._hiabclient.create_targets([targetaddress], targetgroup, dnslookup, scanner)[0]
        tn = TargetNode(targetgroup_node, target)
        targetgroup_node.add_target_node(tn)
        return tn

    def move_target_node(self, target_node, dst_targetgroup_name):
        src_targetgroup_node = target_node.get_parent_targetgroup_node()
        dst_targetgroup_node = self._targetgroups_tree.get_targetgroup_node_from_fq_string(dst_targetgroup_name)
        response = self._hiabclient.move_target(target_node.get_target(), src_targetgroup_node.get_targetgroup(), dst_targetgroup_node.get_targetgroup(), dst_targetgroup_node.get_parent().get_targetgroup())
        if(response):
            target_node.set_parent_targetgroup_node(dst_targetgroup_node)
            src_targetgroup_node.remove_target_node(target_node)
            dst_targetgroup_node.add_target_node(target_node)
            return True
        return False

    def update_target_node(self, target_node, virtualhosts="", scanner_name=None, custom0="", custom1="", custom2="", custom3="", custom4="", custom5="", custom6="", custom7="", custom8="", custom9=""):
        scanner_id = target_node.get_target().scannerid
        if(scanner_name is not None and scanner_name != ""):
            scanner = self._get_scanner_by_name(scanner_name)
            scanner_id = scanner.xid

        target = self._hiabclient.update_target(target = target_node.get_target(), scannerid = scanner_id, virtualhosts = virtualhosts, custom0 = custom0, custom1 = custom1, custom2 = custom2, custom3 = custom3, custom4 = custom4, custom5 = custom5, custom6 = custom6, custom7 = custom7, custom8 = custom8, custom9 = custom9)
        target_node.set_target(target)
        return target_node

    def remove_target_node(self, target_node):
        response = self._hiabclient.delete_targets([target_node.get_target()])
        if(response):
            targetgroup_node = target_node.get_parent_targetgroup_node()
            targetgroup_node.remove_target_node(target_node)
            return True
        return False


    def refresh(self):
        if (not hasattr(self, '_targetgroups_tree')):
            treebuilder = TargetsTreeBuilder(self._hiabclient)
            self._targetgroups_tree = treebuilder.build_tree()

    def get_scanner_by_name(self, scanner_name):
        for s in self._hiabclient.get_scanners():
            if(s.name == scanner_name):
                return s
        return None

    def get_scanner_by_id(self, scanner_id):
        for s in self._hiabclient.get_scanners():
            if(s.xid == scanner_id):
                return s
        return None

class TargetsTreeBuilder:
    
    def __init__(self, op24lib):
        self._hiabclient = op24lib
        self._logger = log.getLogger(__name__)
        self._targetgroups_targets = []

    def build_tree(self):
        targetgroups = self._hiabclient.get_targetgroups()
        self._logger.info("Targetgroups fetched")

        #num_cores = multiprocessing.cpu_count()
     
        for t in targetgroups:
            self._targetgroups_targets.append(self._obtain_targets(t))
        #self._targetgroups_targets = Parallel(n_jobs=num_cores)(delayed(self._obtain_targets)(i) for i in targetgroups)
        self._logger.info("All targetgroups with targets fetched")

        tree = self._build_targetgroup_tree(targetgroups)

        tree.set_depth()

        self._logger.info("Tree has been built")

        self._add_targets_to_tree(tree)
        self._logger.info("Targets to tree added")

        return tree

    def _obtain_targets(self, targetgroup):
        tgs = self._hiabclient.get_targets(targetgroup)
        return (targetgroup, tgs)

    def _build_targetgroup_tree(self, targetgroups):
        lookup = self._make_targetgroup_nodes(targetgroups)

        root = []

        for tgn in lookup:
            parent_tgn = self._lookup_parent(lookup, tgn)
            if(parent_tgn is not None):
                tgn.set_parent(parent_tgn)
                parent_tgn.add_child(tgn)
            else:
                root.append(tgn)
        
        tree = TargetsTree(root[0])
        return tree

    def _lookup_parent(self, proposed_parents, tgn):
        for p in proposed_parents:
            potential_parent_targetgroup = p.get_targetgroup()
            targetgroup = tgn.get_targetgroup()
            if(targetgroup.xiparentid is not None):
                if(targetgroup.xiparentid == potential_parent_targetgroup.xid):
                    return p

    def _make_targetgroup_nodes(self, targetgroups):
        result = []
        for t in targetgroups:
            tgn = TargetGroupNode(t)
            result.append(tgn)
        return result

    def _add_targets_to_tree(self, tree):
        leave_nodes = tree.get_leave_nodes()
        leave_nodes = sorted(leave_nodes, key=lambda n: n.get_depth(), reverse=True)
        deepest_depth = leave_nodes[0].get_depth()
        layers = reversed(range(0, deepest_depth))
        for layer in layers:
            if(layer != 0):
                targetgroups = tree.get_all_targetgroup_nodes_of_depth(layer)
                for tg in targetgroups:
                    self._add_targets_to_targetgroup_node(tg)

        #self._logger.info("Leave nodes fetched")
        #self._add_targets_to_targetgroup_nodes(leave_nodes)
    
    def _add_targets_to_targetgroup_nodes(self, nodes):
        for n in nodes:
            self._add_targets_to_targetgroup_node(n)
        
        parents=[]
        for p in nodes:
            parent_node = p.get_parent()
            if(parent_node is not None and parent_node not in parents):
                parents.append(parent_node)
        
        if(len(parents) > 0):
            self._add_targets_to_targetgroup_nodes(parents)

        self._logger.info("All nodes have been processed.")


    def _add_targets_to_targetgroup_node(self, tgn):
        self._logger.info("Processing targetgroup node: " + tgn.get_targetgroup().name)
        result = []

        targets = self._get_targets_in_targetgroup(tgn.get_targetgroup())

        for t in targets:
            containing_targetnodes = tgn.get_containing_targetnodes_of_target(t)
            if(len(containing_targetnodes) == 0):
                tn = TargetNode(tgn, t)
                tgn.add_target_node(tn)
                result.append(tn)
            else:
                containing_targetgroups_are_all_dynamic = True
                for ctn in containing_targetnodes:
                    if(not(self._is_dynamic_targetgroup(ctn.get_parent_targetgroup_node().get_targetgroup()))):
                        containing_targetgroups_are_all_dynamic = False
                if(containing_targetgroups_are_all_dynamic):
                    tn = TargetNode(tgn, t)
                    tgn.add_target_node(tn)
                    result.append(tn)
    
        self._logger.info("Finished processing node: " + tgn.get_targetgroup().name)
        return result
    
    def _is_dynamic_targetgroup(self, targetgroup):
        if(targetgroup.rulebased or targetgroup.reportbased):
            return True
        return False
    
    def _get_targets_in_targetgroup(self, targetgroup):
        for tuple in self._targetgroups_targets:
            if(targetgroup.xid == tuple[0].xid):
                return tuple[1]

    def _add_targets_to_nodes(self, targetgroup_node):
        targets = self._get_targets_in_targetgroup(targetgroup_node.get_targetgroup())


        for t in targets:
            targetgroup_node.get
            if(not(targetgroup_node.contains_target(t))):
                tn = TargetNode(targetgroup_node, t)
                targetgroup_node.add_target_node(tn)





