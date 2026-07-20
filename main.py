import random
import string
from kivy.app import App
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox

Window.clearcolor=(0.08,0.10,0.16,1)

class CryptaGen(App):
    def build(self):
        self.title="CryptaGen"
        root=BoxLayout(orientation="vertical",padding=20,spacing=10)

        root.add_widget(Label(text="🔐 CryptaGen",font_size=32,bold=True,color=(0.3,0.8,1,1),size_hint=(1,.12)))

        self.aff=Label(text="Appuie sur GÉNÉRER",font_size=28,bold=True,size_hint=(1,.18))
        root.add_widget(self.aff)

        self.lbl=Label(text="Longueur : 16",size_hint=(1,.06))
        root.add_widget(self.lbl)

        self.slider=Slider(min=4,max=64,value=16,step=1,size_hint=(1,.08))
        self.slider.bind(value=lambda i,v:setattr(self.lbl,"text",f"Longueur : {int(v)}"))
        root.add_widget(self.slider)

        self.up=CheckBox(active=True); self.low=CheckBox(active=True)
        self.dg=CheckBox(active=True); self.sp=CheckBox(active=True)

        for cb,name in [(self.up,"Majuscules"),(self.low,"Minuscules"),(self.dg,"Chiffres"),(self.sp,"Symboles")]:
            line=BoxLayout(size_hint=(1,.06))
            line.add_widget(cb); line.add_widget(Label(text=name))
            root.add_widget(line)

        b=Button(text="GÉNÉRER",size_hint=(1,.1))
        b.bind(on_press=self.generer)
        root.add_widget(b)

        c=Button(text="📋 COPIER",size_hint=(1,.1))
        c.bind(on_press=lambda *_: Clipboard.copy(self.aff.text))
        root.add_widget(c)

        self.input=TextInput(hint_text="Entrer un mot de passe à analyser",multiline=False,size_hint=(1,.1))
        root.add_widget(self.input)

        a=Button(text="ANALYSER",size_hint=(1,.1))
        a.bind(on_press=self.analyser)
        root.add_widget(a)

        self.res=Label(text="",font_size=22,size_hint=(1,.1))
        root.add_widget(self.res)
        return root

    def generer(self,*_):
        chars=""
        if self.up.active: chars+=string.ascii_uppercase
        if self.low.active: chars+=string.ascii_lowercase
        if self.dg.active: chars+=string.digits
        if self.sp.active: chars+="!@#$%&*?"
        if not chars:
            self.aff.text="Sélectionne un type"
            return
        self.aff.text="".join(random.choice(chars) for _ in range(int(self.slider.value)))

    def analyser(self,*_):
        p=self.input.text
        score=0
        if len(p)>=8: score+=1
        if len(p)>=12: score+=1
        if any(c.islower() for c in p): score+=1
        if any(c.isupper() for c in p): score+=1
        if any(c.isdigit() for c in p): score+=1
        if any(c in "!@#$%^&*()-_=+[]{};:,.?/\\|" for c in p): score+=1
        if score<=2:
            self.res.text="🔴 Faible"; self.res.color=(1,0,0,1)
        elif score<=4:
            self.res.text="🟡 Moyen"; self.res.color=(1,1,0,1)
        else:
            self.res.text="🟢 Fort"; self.res.color=(0,1,0,1)

CryptaGen().run()
class CryptaGen(App):
    icon = "icon.png"
