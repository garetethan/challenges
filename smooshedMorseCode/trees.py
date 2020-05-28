class Node():
	'''Generic node in a tree.'''
	def __init__(self, parent, data, children=None):
		self.parent = parent
		self.data = data
		self.children = children if children else []
	
	@classmethod
	def root(cls, data=None):
		return cls(None, data, [])
	
	def clone(self):
		'''
		Assumes that data supports .clone().
		Clone has separate children from original but shares the same parent.
		'''
		return Node(self.parent, self.data.clone(), self.children.clone())
	
	def addChild(self, data):
		newChild = Node(self, data, [])
		self.children.append(newChild)
		return newChild
	
	def __eq__(self, other):
		return self.data == other.data
	
	def __lt__(self, other):
		return self.data < other.data
	
	def __le__(self, other):
		return self.data <= other.data
	
	def __gt__(self, other):
		return self.data > other.data
	
	def __ge__(self, other):
		return self.data >= other.data
	
	def __str__(self):
		print(f'Node with data: {self.data}.')
	
	def __repr__(self):
		print(f'Node({self.parent}, {self.data}, {self.children})')
	
	def __hash__(self):
		return hash(self.data)
