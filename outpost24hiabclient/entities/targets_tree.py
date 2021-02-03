class TargetsTree:
    
    def __init__(self, root_node):
        self._root_node = root_node

    def __repr__(self):
        return "Tree\n" + repr(self._root_node)

    def get_root_node(self):
        return self._root_node

    def get_leave_nodes(self, subtree=None):
        if(subtree is None):
            return self.get_leave_nodes(self._root_node)
        else:
            result = []
            if(not subtree.get_childs()):
                result.append(subtree)
                return result
            else:
                childs = subtree.get_childs()
                for c in childs:
                    result = result + self.get_leave_nodes(c)
                return result
    
    def get_all_targetgroup_nodes(self):
        return self._root_node.get_descending_targetgroup_nodes()

    def get_all_target_nodes(self):
        return self._root_node.get_descending_target_nodes()

    def get_all_targetgroup_nodes_of_depth(self, depth):
        result = []
        all_tg_nodes = [self._root_node]
        desc_nodes = self._root_node.get_descending_targetgroup_nodes()
        all_tg_nodes.extend(desc_nodes)
        for t in all_tg_nodes:
            if(t.get_depth() == depth):
                result.append(t)
        return result

    def get_targetgroup_node_from_fq_string(self, fq):
        if(fq is None):
            return None
        if(fq == ""):
            return None

        targetgroupnamecomponents = fq.split('\\')

        targetgroup_node = self._root_node
        i=1
        while(i<len(targetgroupnamecomponents)-1):
            root_targetgroup_name = targetgroupnamecomponents[i]
    
            if(targetgroup_node is None):
                return None
            elif(targetgroup_node.get_targetgroup().name == root_targetgroup_name):
                child_targetgroup_name = targetgroupnamecomponents[i+1]
                child = targetgroup_node.get_child_with_name(child_targetgroup_name)
                targetgroup_node = child
            i = i+1

        return targetgroup_node

    def get_target_node(self, ipaddress, hostname, scanner, targetgroupfq = None):

        if((ipaddress is None or ipaddress == "") and (hostname is None or hostname == "")):
            return None
        if(scanner is None):
            return None
        
        if(targetgroupfq is None or targetgroupfq == ""):
            target_nodes = self.get_all_target_nodes()
            return self._select_target_node(target_nodes, ipaddress, hostname, scanner)
        else:
            targetgroup_node = self.get_targetgroup_node_from_fq_string(targetgroupfq)
            if(targetgroup_node is None):
                return None
            else:
                target_nodes = targetgroup_node.get_target_nodes()
                return self._select_target_node(target_nodes, ipaddress, hostname, scanner)
        return None
    
    def _select_target_node(self, target_nodes, ipaddress, hostname, scanner):
        for t in target_nodes:
            target = t.get_target()
            if(not(ipaddress == "") and target.ipaddress is not None):
                if(ipaddress == target.ipaddress and scanner.xid == target.scannerid):
                    return t
            if(not(hostname == "") and target.hostname is not None):
                if(hostname == target.hostname and scanner.xid == target.scannerid):
                    return t

    def get_target_nodes_by_ipaddress(self, ipaddress):
        result = []
        tgn = self._root_node.get_descending_target_nodes()
        for tn in tgn:
            target = tgn.get_target()
            if(target.ipaddress == ipaddress):
                result.append(tn)
        return result

    def get_target_nodes_by_hostname(self, hostname):
        result = []
        tgn = self._root_node.get_descending_target_nodes()
        for tn in tgn:
            target = tgn.get_target()
            if(target.hostname == hostname):
                result.append(tn)
        return result

    def set_depth(self):
        self._root_node.set_depth(0)

class TargetGroupNode:

    def __init__(self, targetgroup, parent=None, childs=None):
        self._targetgroup = targetgroup
        self._parent = parent
        if(childs is not None):
            self._childs = childs
        else:
            self._childs = []
        self._target_nodes = []
        self._depth=-1

    def __repr__(self):
        return "TargetGroupNode(XID: " +str(self._targetgroup.xid)+ ", Name: "+ self._targetgroup.name + ", \n" + repr(self._childs) + ", \n" + repr(self._target_nodes) + ")\n"

    def get_targetgroup(self):
        return self._targetgroup
    
    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent

    def get_childs(self):
        return self._childs

    def get_child_with_name(self, targetgroup_name):
        for c in self._childs:
            if(c.get_targetgroup().name == targetgroup_name):
                return c

    def add_child(self, child):
        if(child not in self._childs):
            self._childs.append(child)

    def get_target_nodes(self):
        return self._target_nodes

    def add_target_node(self, target):
        self._target_nodes.append(target)

    def get_descending_targetgroup_nodes(self):
        result = []
        childs = self.get_childs()
        for c in childs:
            result.append(c)
            desc_childs = c.get_descending_targetgroup_nodes()
            result.extend(desc_childs)
        return result

    def get_descending_target_nodes(self):
        result = []
        target_nodes = self.get_target_nodes()
        result.extend(target_nodes)
        for c in self.get_childs():
            result.extend(c.get_descending_target_nodes())
        return result

    def get_containing_targetnodes_of_target(self, target):
        result = []
        target_nodes = self.get_descending_target_nodes()
        for tn in target_nodes:
            tnt = tn.get_target()
            if(target.xid == tnt.xid):
                result.append(tn)
        return result

    def contains_target(self, target):
        target_nodes = self.get_descending_target_nodes()
        for tn in target_nodes:
            tnt = tn.get_target()
            if(target.xid == tnt.xid):
                return True
        return False

    def get_fq_string(self):
        result = "\\" + self.get_targetgroup().name
        parent = self.get_parent()
        while(parent is not None):
            result = "\\" + parent.get_targetgroup().name + result
            parent = parent.get_parent()
        return result

    def get_depth(self):
        return self._depth

    def set_depth(self, depth):
        self._depth = depth
        for c in self.get_childs():
            c.set_depth(depth+1)

    def remove_target_node(self, target_node):
        self._target_nodes.remove(target_node)

class TargetNode:

    def __init__(self, parent_targetgroup_node, target):
        self._target = target
        self._parent_targetgroup_node = parent_targetgroup_node

    def __repr__(self):
        if(self._target.ipaddress is not None):
            return "TargetNode(XID: " +str(self._target.xid)+ ", hostname: "+self._target.ipaddress+")"
        elif(self._target.hostname is not None):
            return "TargetNode(XID: " +str(self._target.xid)+ ", hostname: "+self._target.hostname+")"
        else:
            return "TargetNode(XID: " +str(self._target.xid)+ ")"

    def get_parent_targetgroup_node(self):
        return self._parent_targetgroup_node

    def get_target(self):
        return self._target

    def set_parent_targetgroup_node(self, parent_targetgroup_node):
        self._parent_targetgroup_node = parent_targetgroup_node

    def set_target(self, target):
        self._target = target
