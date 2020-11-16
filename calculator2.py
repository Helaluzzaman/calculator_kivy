from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import re

class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__( **kwargs)
		self.cols = 1
		self.input = TextInput(font_size = 30)
		self.add_widget(self.input)
		
		self.inside = GridLayout()
		self.inside.cols = 4

		# number buttons 7 8 9
		self.seven = Button(text = "7", font_size = 50)
		self.seven.bind(on_press = self.sevend)
		self.inside.add_widget(self.seven)

		self.eight = Button(text = "8", font_size = 50)
		self.eight.bind(on_press = self.eightd)
		self.inside.add_widget(self.eight)

		self.nine = Button(text = "9", font_size = 50)
		self.nine.bind(on_press = self.nined)
		self.inside.add_widget(self.nine)
		

		self.div = Button(text = "/", font_size = 50)
		self.div.bind(on_press = self.dividing)
		self.inside.add_widget(self.div)

		self.four = Button(text = "4", font_size = 50)
		self.four.bind(on_press = self.fourd)
		self.inside.add_widget(self.four)

		self.five = Button(text = "5", font_size = 50)
		self.five.bind(on_press = self.fived)
		self.inside.add_widget(self.five)

		self.six = Button(text = "6", font_size = 50)
		self.six.bind(on_press = self.sixd)
		self.inside.add_widget(self.six)

		self.mul = Button(text = "*", font_size = 50)
		self.mul.bind(on_press = self.multiply)
		self.inside.add_widget(self.mul)

		# number 1, 2, 3
		self.one = Button(text = "1", font_size = 50)
		self.one.bind(on_press = self.oned)
		self.inside.add_widget(self.one)

		self.two = Button(text = "2", font_size = 50)
		self.two.bind(on_press = self.twod)
		self.inside.add_widget(self.two)

		self.three = Button(text = "3", font_size = 50)
		self.three.bind(on_press = self.threed)
		self.inside.add_widget(self.three)

		self.sub = Button(text = "-", font_size = 50)
		self.sub.bind(on_press = self.subtract)
		self.inside.add_widget(self.sub)

		#blank
		self.open_parentesis= Button(text = "(", font_size= 50)
		self.open_parentesis.bind(on_press = self.openingp)
		self.inside.add_widget(self.open_parentesis)

		self.zero = Button(text = "0", font_size = 50)
		self.zero.bind(on_press = self.zerod)
		self.inside.add_widget(self.zero)

		self.point = Button(text = ".", font_size = 50)
		self.point.bind(on_press = self.pointd)
		self.inside.add_widget(self.point)



		# control buttons.
		self.add = Button(text = "+", font_size = 50)
		self.add.bind(on_press = self.adding)
		self.inside.add_widget(self.add)

		#blank
		self.close_parentesis= Button(text = ")", font_size= 50)
		self.close_parentesis.bind(on_press = self.closingp)
		self.inside.add_widget(self.close_parentesis)

		self.back= Button(text = "back", font_size = 30)
		self.back.bind(on_press = self.backing)
		self.inside.add_widget(self.back)

		self.clear = Button(text = "clear", font_size = 30)
		self.clear.bind(on_press = self.clearing)
		self.inside.add_widget(self.clear)

		self.equal = Button(text = "=", font_size = 50)
		self.equal.bind(on_press = self.resulting)
		self.inside.add_widget(self.equal)

		self.add_widget(self.inside)

	def oned(self, instance):
		self.input.text += "1"
	def twod(self, instance):
		self.input.text += "2"
	def threed(self, instance):
		self.input.text += "3"
	def fourd(self, instance):
		self.input.text += "4"
	def fived(self, instance):
		self.input.text += "5"
	def sixd(self, instance):
		self.input.text += "6"
	def sevend(self, instance):
		self.input.text += "7"
	def eightd(self, instance):
		self.input.text += "8"
	def nined(self, instance):
		self.input.text += "9"
	def zerod(self, instance):
		self.input.text += "0"
	def pointd(self, instance):
		self.input.text += "."

	def adding(self, instance):
		self.input.text += "+"
	def subtract(self, instance):
		self.input.text += "-"
	def multiply(self, instance):
		self.input.text += "*"
	def dividing(self, instance):
		self.input.text += "/"
	def clearing(self, instance):
		self.input.text = ""
	def openingp(self, instance):
		self.input.text += "("
	def closingp(self, instance):
		self.input.text += ")"
	def backing(self, instance):
		self.input.text = self.input.text[:-1]

# result function so it can be complex
	def resulting(self, instance):
		rdata = self.input.text
		pattern = r"\n?(.+)$"
		rslt = re.findall(pattern, rdata)
		try :
			data = rslt[0]
		except:
			data = ""
		try: 
			result = eval(data)
			self.input.text += " = "
		except :
			result = "Invalid input"
		self.input.text += str(result)
		self.input.text += "\n"


class Calculator(App):
	def build(self):
		return MyGrid()

if __name__ == "__main__":
	Calculator().run()