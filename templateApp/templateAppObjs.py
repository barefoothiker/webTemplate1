class ListPlotObj(object):
	def __init__(self):

		self.title = 0        
		self.index = 0
		
		self.algorithm = ""
		self.aucs = []
		
		self.columns = []
		self.rows = []
	
	def __unicode__(self):
		return str(self.columns)
    
class ValueObj(object):
	def __init__(self):

		self.xValue = 0        
		self.yValue = 0
		
		self.colorValue = ""
	
	def __unicode__(self):
		return str(self.xValue)