#!/usr/bin/env python3

class Field(object):
	"""docstring for Field"""
	def __init__(self, name, column_type):
		super(Field, self).__init__()
		self.name = name
		self.column_type = column_type
		
	def __str__(self):
		print('<%s:%s>' % (self.__class__.__name__, self.name))

class IntegerField(Field):
	"""docstring for IntegerField"""
	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'int')
		
class StringField(Field):
	"""docstring for StringField"""
	def __init__(self, name):
		super(StringField, self).__init__(name, 'string')

class Modelmetaclass(type): # type
	"""docstring for Modelmetaclass"""
	def __new__(cls, name, bases, attrs):
		if name == 'Model':
			return type.__new__(cls, name, bases, attrs)
		print('Found name:%s' % name)
		mappings = dict() # save mappings of attributes
		for i, j in attrs.items():
			if isinstance(j, Field):
				print('mapping: %s ==> %s' % (i, j))
				mappings[i] = j # name i => 'Field'
		for i in mappings.keys():
			attrs.pop(i) # delete attrs that have been transfer to 'Field'
		attrs['__mappings__'] = mappings 
		attrs['__table__'] = name 
		return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=Modelmetaclass):
	"""docstring for Model"""
	# reuse the old definitions of functions
	def __init__(self, **kw):
		super(Model, self).__init__(**kw)
		
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

	def save(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self, k, None))
		sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
		print('SQL: %s' % sql)
		print('ARGS: %s' % str(args))

# User provide the interfaces
class User(Model):
	id = IntegerField('id')
	name = StringField('username')
	email = StringField('email')
	password = StringField('password')

def main():
	# Create an object
	u = User(id=9, name='Wasdns', email='952693358@qq.com', password='1234567')
	# Save the object in the Database
	u.save()

if __name__ == '__main__':
	main()