=====
Usage
=====

To use outpost24hiabclient in a project:

.. code-block:: python
  # Working with users and usergroups
	from outpost24hiabclient import Users
	from outpost24hiabclient.entities.user import User
	from outpost24hiabclient.entities.usergroup import UserGroup
	
	# enumerate users in Outpost24 HIAB
	user_service = Users(url, token)
	users = user_service.get_users()
	for user in users:
		print(user.vcusername)

    # enumerate usergroups in Outpost24 HIAB
	groups = user_service.get_usergroups()
	for group in groups:
		print(group.vcname)
	
	# create a user
	user = user_service.create_user(FIRST_NAME,
								LAST_NAME,
								EMAIL,
								PHONENUMBER,
								COUNTRY,
								USERNAME,
								PASSWORD,
								usergrouplist = [USERGROUP1_OBJECT],
								targetlist = [TARGET1_OBJECT],
								scannerlist = [SCANNER1_OBJECT])
	
	# delete users
	isdeleted = user_service.delete_users([USER_OBJECT])
	

	# Working with scanners
	from outpost24hiabclient import Scanners
	from outpost24hiabclient.entities.scanner import Scanner
	
	# enumerate scanners in Outpost24 HIAB
	scanner_service = Scanners(url, token)
	scanners = scanner_service.get_scanners()

	
	# Working with targets and targetgroups
	from outpost24hiabclient import Targets
	from outpost24hiabclient.entities.target import Target
	from outpost24hiabclient.entities.targetgroup import TargetGroup
	from outpost24hiabclient.entities.targets_tree import TargetsTree
	from outpost24hiabclient.entities.targets_tree import TargetGroupNode
	from outpost24hiabclient.entities.targets_tree import TargetNode
	
	# enumerate targetgroups in Outpost24 HIAB
	target_service = Targets(url, token)
	targetgroup_nodes = target_service.get_targetgroup_nodes()
	for targetgroup_node in targetgroup_nodes:
		print(targetgroup_node.get_targetgroup().name)

	# get the parent targetgroup of a targetgroup_node
	for targetgroup_node in targetgroup_nodes:
		print(targetgroup_node.get_targetgroup().name)
	
	# enumerate targets
	target_nodes = target_service.get_targets()
	for target in targets:
		print(target.hostname)
	
	# get targets in a particular targetgroup
	target_nodes = targetgroup_node.get_target_nodes()
	for target_node in target_nodes:
		print(target_node.get_target().hostname)
	
	# create targetgroup node
	targetgroup_name = "\\All targets\\testgroup1\\testgroup2"
	target_node = target_service.create_targetgroup_from_fq_string(targetgroup_name)
	
	# create target
	target_node = target_service.create_target_node(target_address, targetgroup_name, scanner_name, dnslookup=True)
										
	# delete targets
	isremoved = target_service.remove_target_node(target_node)
	
	
