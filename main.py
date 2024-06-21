import kivy
import os
import pygame
import random
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.card import MDCard
from kivy.app import App
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
import arabic_reshaper
from bidi.algorithm import get_display
from random import sample 
from random import shuffle
from random import choice
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex
from kivy.graphics import Color
from kivy.graphics import RoundedRectangle
from kivy.metrics import dp
from kivy.core.window import Window

pygame.mixer.init()

lessons = {
    'Lesson 1': [
        {'word': 'abandon', 'meaning': 'دست کشیدن ,  ترک کردن','pronunciation': '/əbændən/', 'synonym': 'desert', 'example': 'When Roy abandoned his family, the police went looking for him.'},
        {'word': 'keen', 'meaning': 'تیز , مشتاق','pronunciation': '/kin/', 'synonym': 'sharp ، acute', 'example': 'The butcher’s keen knife cut through the meat.'},
        {'word': 'jealous', 'meaning': 'حسود','pronunciation': '/dʒeləs/', 'synonym': 'envious', 'example': 'Although my neighbor bought a new car, I’m not jealous of him.'},
        {'word': 'tact', 'meaning': 'تدبیر , درایت','pronunciation': '/tækt/', 'synonym': 'ability to say somthing', 'example': 'By the use of tact, Janet was able to calm her jealous husband.'},
        {'word': 'oath', 'meaning': 'سوگند , دشنام','pronunciation': '/oʊθ/', 'synonym': 'promis', 'example': 'In court, the witness took an oath that he would tell the truth.'},
        {'word': 'vacant', 'meaning': 'خالی , تهی','pronunciation': '/vekənt/', 'synonym': 'empty', 'example': 'I put my coat on that vacant seat.'},
        {'word': 'hardship', 'meaning': 'سختی , دشواری','pronunciation': '/hrdʃp/', 'synonym': 'difficulty', 'example': 'Abe Lincoln was able to overcome one hardship after anothe.'},
        {'word': 'gallant', 'meaning': 'شجاع','pronunciation': '/gælənt/', 'synonym': 'brave', 'example': 'Many gallant knights entered the contest to win the princess.'},
        {'word': 'data', 'meaning': 'اطلاعات','pronunciation': '/detə/', 'synonym': 'facts', 'example': 'The data about the bank robbery were given to the F.B.I.'},
        {'word': 'unaccustomed', 'عادت نداشتن': 'سیب','pronunciation': '/ˌʌnəkʌstəmd/', 'synonym': 'not used to somthing', 'example': 'The king was unaccustomed to having people disobey him.'},
        {'word': 'bachelor', 'meaning': 'مجرد','pronunciation': '/bætʃələr/', 'synonym': 'a man who has not married', 'example': 'In the movie, the married man was mistaken for a bachelor.'},
        {'word': 'qualify', 'meaning': 'صلاحیت داشتن , واجد شرایط بودن','pronunciation': '/kwlfa/', 'synonym': 'fruit', 'example': 'I am trying to qualify for the job that is now vacant.'}
    ],
    'Lesson 2': [
        {'word': 'corpse', 'meaning': 'جسد , جنازه','pronunciation': '/kɔrps/', 'synonym': 'body', 'example': 'The corpse was laid to rest in the vacant coffin.'},
        {'word': 'conceal', 'meaning': 'مخفی کردن','pronunciation': '/kənsil/', 'synonym': 'hide', 'example': 'Tris couldn’t conceal his love for Gloria.'},
        {'word': 'dismal', 'meaning': ' دلگیر , تاریک','pronunciation': '/dzməl/', 'synonym': 'depressing', 'example': 'When the weather is dismal, I stay in bed.'},
        {'word': 'frigid', 'meaning': 'خیلی سرد','pronunciation': '/frʤəd/', 'synonym': 'icy', 'example': 'Inside the butcher’s freezer the temperature was frigid.'},
        {'word': 'inhabit', 'meaning': 'زندگی کردن ,اقامت داشتن','pronunciation': '/nhæbət/', 'synonym': 'live', 'example': 'Eskimos inhabit the frigid part of Alaska.'},
        {'word': 'numb', 'meaning': 'کرخت , بی حس','pronunciation': '/nʌm/', 'synonym': 'figid', 'example': 'My finger quickly became numb in the frigid room.'},
        {'word': 'peril', 'meaning': 'خطر','pronunciation': '/perəl/', 'synonym': 'danger', 'example': 'There is great peril in trying to climb the mountain.'},
        {'word': 'recline', 'meaning': 'دراز کشیدن','pronunciation': '/rklan/', 'synonym': 'sleep', 'example': 'Richard likes to recline in front of the TV.'},
        {'word': 'shriek', 'meaning': ' فریاد , جیغ زدن','pronunciation': '/ʃrik/', 'synonym': 'scream', 'example': 'With a load shriek, Ronald fled from the room.'},
        {'word': 'sinister', 'meaning': 'پلید , شوم','pronunciation': '/snəstər/', 'synonym': 'evil', 'example': 'I was frightened by the sinister shadow at the bottom of the stairs.'},
        {'word': 'tempt', 'meaning': 'وسوسه کردن  , اغوا کردن','pronunciation': '/tempt/', 'synonym': 'try to get someone to get something', 'example': 'Your offer of a job tempts me greatly.'},
        {'word': 'wager', 'meaning': 'شرط , شرط بندی','pronunciation': '/wedʒər/', 'synonym': 'bet', 'example': 'I lost a small wager on the Super BowL.'},
        
    ],
    'Lesson 3': [
        {'word': 'typical', 'meaning': 'معمول , عادی','pronunciation': '/tpkl/', 'synonym': 'usual', 'example': 'It was typical of the latecomer to conceal the real cause of his lateness.'},
        {'word': 'minimum', 'meaning': 'کمترین  , حداقل','pronunciation': '/mnməm/', 'synonym': 'less', 'example': 'Congress has set a minimum wage for all workers.'},
        {'word': 'scarce', 'meaning': ' نادر , کمیاب','pronunciation': '/skers/', 'synonym': 'nothing', 'example': 'How scarce of good cooks?.'},
        {'word': 'annual', 'meaning': 'سالیانه','pronunciation': '/ænjuəl/', 'synonym': 'year', 'example': 'The annual convention of musicians takes place in Hollywood.'},
        {'word': 'persuade', 'meaning': 'متقاعد کردن','pronunciation': '/pərswed/', 'synonym': 'convince', 'example': 'No one could persuade the captain to leave the sinking ship.'},
        {'word': 'essential', 'meaning': 'ضروری','pronunciation': '/senʃl/', 'synonym': 'necessary', 'example': 'It is essential that we follow the road map.'},
        {'word': 'blend', 'meaning': 'ترکیب کردن  , مخلوط کردن','pronunciation': '/blend/', 'synonym': 'put anything with each other', 'example': 'The colors of the rainbow blend into one another.'},
        {'word': 'visible', 'meaning': 'نمایان , پیدا','pronunciation': '/vzəbl/', 'synonym': 'obvious', 'example': 'The ship was barely visible through the dense fog.'},
        {'word': 'expensive', 'meaning': 'گران','pronunciation': '/kspensv/', 'synonym': 'not cheap', 'example': 'BMW is much expensive than Chevy.'},
        {'word': 'talent', 'meaning': 'استعداد','pronunciation': '/tælənt/', 'synonym': 'the work your are better than other', 'example': 'Hard work can often make up for a lack of talent.'},
        {'word': 'devise', 'meaning': '	اختراع کردن','pronunciation': '/dvaz/', 'synonym': 'new tools', 'example': 'The burglars devised a scheme for entering the bank at night.'},
        {'word': 'wholesale', 'meaning': 'عمده  , عمده فروشی','pronunciation': '/hoʊlsel/', 'synonym': 'store', 'example': 'The wholesale price of milk is six cents.'}  
    ],
    'Lesson 4':[
        {'word': 'vapor', 'meaning': 'بخار','pronunciation': '/vepər/', 'synonym': 'wet', 'example': 'It was typical of the latecomer to conceal the real cause of his lateness.'},
        {'word': 'eliminate', 'meaning': 'حذف کردن','pronunciation': '/lmnet/', 'synonym': 'dead', 'example': 'Congress has set a minimum wage for all workers.'},
        {'word': 'villain', 'meaning': 'آدم شرور و پست','pronunciation': '/vlən/', 'synonym': 'evil', 'example': 'How scarce of good cooks?'},
        {'word': 'dense', 'meaning': 'متراکم , انبوه','pronunciation': '/dens/', 'synonym': 'thick', 'example': 'The annual convention of musicians takes place in Hollywood.'},
        {'word': 'utilize', 'meaning': 'استفاده کردن  , بکار بردن','pronunciation': '/jutəlaz/', 'synonym': 'make use of', 'example': 'No one could persuade the captain to leave the sinking ship.'},
        {'word': 'humid', 'meaning': 'مرطوب  , شرجی','pronunciation': '/hjumd/', 'synonym': 'moist', 'example': 'It is essential that we follow the road map.'},
        {'word': 'theory', 'meaning': 'نظریه  , فرضیه','pronunciation': '/θiəri/', 'synonym': 'explain', 'example': 'The colors of the rainbow blend into one another.'},
        {'word': 'descend', 'meaning': 'فرود آمدن , پایین رفتن','pronunciation': '/dsend/', 'synonym': 'go or come down', 'example': 'The ship was barely visible through the dense fog.'},
        {'word': 'circulate', 'meaning': 'چرخیدن پخش کردن','pronunciation': '/sɜrkjəlet/', 'synonym': 'circle', 'example': 'BMW is much expensive than Chevy.'},
        {'word': 'enormous', 'meaning': 'بی نهایت بزرگ','pronunciation': '/nɔrməs/', 'synonym': 'huge', 'example': 'Hard work can often make up for a lack of talent.'},
        {'word': 'predict', 'meaning': 'پیش بینی کردن','pronunciation': '/prdkt/', 'synonym': 'forecast', 'example': 'The burglars devised a scheme for entering the bank at night.'},
        {'word': 'vanish', 'meaning': 'محو شدن , ناپدید شدن','pronunciation': '/vænʃ/', 'synonym': 'cant see them', 'example': 'The wholesale price of milk is six cents'}
    ],
    'Lesson 5':[
        {'word': 'tradition', 'meaning': 'سنت , رسم','pronunciation': '/trədʃn/', 'synonym': 'beliefs', 'example': 'All religions have different beliefs and traditions.'},
        {'word': 'rural', 'meaning': 'روستایی','pronunciation': '/rʊrəl/', 'synonym': 'in the country', 'example': 'Rural areas are not densely populated.'},
        {'word': 'burden', 'meaning': 'بار سنگینی','pronunciation': '/bɜrdn/', 'synonym': 'a load', 'example': 'Irma found the enormous box too much of a burden.'},
        {'word': 'campus', 'meaning': 'محوطه فضای دانشگاه','pronunciation': '/kæmpəs/', 'synonym': 'univercity or school', 'example': 'I chose to go to Penn State because it has a beautiful campus.'},
        {'word': 'majority', 'meaning': 'اکثریت','pronunciation': '/mədʒɔrəti/', 'synonym': 'minority', 'example': 'A majority of votes was needed for the bill to pass.'},
        {'word': 'assemble', 'meaning': 'جمع آوری کردن , مونتاژ کردن','pronunciation': '/əsembl/', 'synonym': 'bring toghther', 'example': 'I am going to assemble a model of a spacecraft.'},
        {'word': 'explore', 'meaning': 'بررسی کردن , کاوش کردن','pronunciation': '/ksplɔr/', 'synonym': 'analyze', 'example': 'The weather bureau explored the effects of the rainy weather.'},
        {'word': 'topic', 'meaning': 'مبحث , موضوع','pronunciation': '/tpk/', 'synonym': 'subject', 'example': 'Valerie only discussed topics that she knew well.'},
        {'word': 'debate', 'meaning': 'بحث , مناظره','pronunciation': '/dbet/', 'synonym': 'conversation', 'example': 'Debate in the U.S Senate lasted for five days.'},
        {'word': 'evade', 'meaning': 'گریختن , طفره رفتن','pronunciation': '/ved/', 'synonym': 'run', 'example': 'Juan tried to evade the topic by changing the subject.'},
        {'word': 'probe', 'meaning': 'کاوش کردن , تحقیق کردن','pronunciation': '/proʊb/', 'synonym': 'investigate', 'example': 'The lawyer probed the man’s mind to see if he was innocent.'},
        {'word': 'reform', 'meaning': 'بهبود بخشیدن , اصلاح کردن','pronunciation': '/rfɔrm/', 'synonym': 'make the better', 'example': 'After the prison riot, the council decided to reform the correctional system.'}
    ],
    'Lesson 6':[],
    'Lesson 7':[],
    'Lesson 8':[],
    'Lesson 9':[],
    'Lesson 10':[],
    'Lesson 11':[],
    'Lesson 12':[],
    'Lesson 13':[],
    'Lesson 14':[],
    'Lesson 15':[],
    'Lesson 16':[],
    'Lesson 17':[],
    'Lesson 18':[],
    'Lesson 19':[],
    'Lesson 20':[],
    'Lesson 21':[],
    'Lesson 22':[],
    'Lesson 23':[],
    'Lesson 24':[],
    'Lesson 25':[],
    'Lesson 26':[],
    'Lesson 27':[],
    'Lesson 28':[],
    'Lesson 29':[],
    'Lesson 30':[],
    'Lesson 31':[],
    'Lesson 32':[],
    'Lesson 33':[],
    'Lesson 34':[],
    'Lesson 35':[],
    'Lesson 36':[],
    'Lesson 37':[],
    'Lesson 38':[],
    'Lesson 39':[],
    'Lesson 40':[],
    'Lesson 41':[],
    'Lesson 42':[]  
}

my_words = []

class EnterNameScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = MDLabel(
            text="Enter your name",
            halign="center",
            theme_text_color="Primary"
        )

        self.text_field = MDTextField(
            hint_text="Name",
            mode="rectangle",
            size_hint=(0.8, None),
            height=30,
            pos_hint={"center_x": 0.5}
        )

        self.next_button = MDRaisedButton(
            text="Next",
            pos_hint={"center_x": 0.5},
            on_release=self.next_screen
        )

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.text_field)
        self.layout.add_widget(self.next_button)

        self.add_widget(self.layout)

    def next_screen(self, instance):
        self.manager.current = 'enter_age'

class EnterAgeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = MDLabel(
            text="Enter your age",
            halign="center",
            theme_text_color="Primary"
        )

        self.text_field = MDTextField(
            hint_text="Age",
            mode="rectangle",
            size_hint=(0.8, None),
            height=30,
            pos_hint={"center_x": 0.5},
            input_filter="int"
        )

        self.next_button = MDRaisedButton(
            text="Next",
            pos_hint={"center_x": 0.5},
            on_release=self.next_screen
        )

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.text_field)
        self.layout.add_widget(self.next_button)

        self.add_widget(self.layout)

    def next_screen(self, instance):
        self.manager.current = 'enter_email'

class EnterEmailScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)

        self.label = MDLabel(
            text="Enter your email",
            halign="center",
            theme_text_color="Primary"
        )

        self.text_field = MDTextField(
            hint_text="Email",
            mode="rectangle",
            size_hint=(0.8, None),
            height=30,
            pos_hint={"center_x": 0.5},
            input_type="mail"
        )

        self.next_button = MDRaisedButton(
            text="Next",
            pos_hint={"center_x": 0.5},
            on_release=self.next_screen
        )

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.text_field)
        self.layout.add_widget(self.next_button)

        self.add_widget(self.layout)

    def next_screen(self, instance):
        self.manager.current = 'guide'

class GuideScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = MDLabel(
            text="Welcome to the 504 Essential Words Guide",
            halign="center",
            theme_text_color="Primary"
        )
        
        self.text = MDLabel(
            text="This application helps you learn and memorize 504 essential words...",
            halign="center",
            theme_text_color="Secondary"
        )
        
        self.finish_button = MDRaisedButton(
            text="Finish",
            pos_hint={"center_x": 0.5},
            on_release=self.finish_screen
        )
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.text)
        self.layout.add_widget(self.finish_button)
        
        self.add_widget(self.layout)
        
    def finish_screen(self, instance):
        self.manager.current = 'main'

class WordScreen(MDScreen):
    def __init__(self, name, word_info, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.word_info = word_info
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(self.layout)
        self.show_word()

    def show_word(self):
        self.layout.clear_widgets()

        # Word Label
        reshaped_word = arabic_reshaper.reshape(self.word_info['word'])
        bidi_word = get_display(reshaped_word)
        word_label = MDLabel(text=bidi_word, halign='center', font_style='H4', size_hint_y=None)
        self.layout.add_widget(word_label)

        # Meaning Label
        reshaped_text = arabic_reshaper.reshape(self.word_info['meaning'])
        bidi_text=get_display(reshaped_text) 
        persian_label = Label(
            text=bidi_text, 
            font_name='B-NAZANIN.ttf',
            halign='right',
            text_size=(self.width, None)
            , font_size='18sp',
            color=[1,0,0,1]  
        )
        self.layout.add_widget(persian_label)

        # Synonym and Example Labels
        reshaped_synonym = arabic_reshaper.reshape(self.word_info['synonym'])
        bidi_synonym = get_display(reshaped_synonym)
        synonym_label = MDLabel(text=f"Synonym: {bidi_synonym}", halign='center', size_hint_y=None)
        self.layout.add_widget(synonym_label)

        reshaped_example = arabic_reshaper.reshape(self.word_info['example'])
        bidi_example = get_display(reshaped_example)
        example_label = MDLabel(text=f"Example: {bidi_example}", halign='center', size_hint_y=None)
        self.layout.add_widget(example_label)

        # Image
        image_path = f"C:/Users/REMIS/Desktop/504/image/{self.word_info['word']}.jpg"
        if os.path.exists(image_path):
            word_image = Image(source=image_path)
            self.layout.add_widget(word_image)

        # Play Pronunciation Button
        play_button = MDRaisedButton(text="Play Pronunciation", size_hint=(1, None), height='50dp')
        play_button.bind(on_release=self.play_pronunciation)
        self.layout.add_widget(play_button)

        # Back and Add Button Layout
        button_layout = BoxLayout(size_hint_y=None, height='50dp', padding=10, spacing=10)
        back_button = MDRaisedButton(text='Back', size_hint=(1, None), height='50dp')
        back_button.bind(on_release=self.go_back)
        button_layout.add_widget(back_button)

        add_button = MDRaisedButton(text='Add', size_hint=(1, None), height='50dp')
        add_button.bind(on_release=self.add_to_my_words)
        button_layout.add_widget(add_button)

        self.layout.add_widget(button_layout)

    def play_pronunciation(self, instance):
        try:
            audio_file = f"C:/Users/REMIS/Desktop/504/audio/{self.word_info['word']}.mp3"
            pygame.mixer.music.load(audio_file)
            pygame.mixer.music.play()
        except pygame.error as e:
            print(f"Error playing audio: {e}")

    def go_back(self, instance):
        self.manager.current = self.manager.previous()

    def add_to_my_words(self, instance):
        if self.word_info not in my_words:
            my_words.append(self.word_info)
        self.manager.current = self.manager.previous()

class LessonScreen(MDScreen):
    def __init__(self, lesson_name, **kwargs):
        super().__init__(**kwargs)
        self.lesson_name = lesson_name
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(self.layout)
        self.show_lesson()

    def show_lesson(self):
        self.layout.clear_widgets()

        # Scroll View for words
        scroll_view = ScrollView(size_hint=(1, 1), do_scroll_x=False, do_scroll_y=True)
        words_layout = GridLayout(cols=1, size_hint_y=None, padding=10, spacing=10)
        words_layout.bind(minimum_height=words_layout.setter('height'))

        for word_info in lessons[self.lesson_name]:
            reshaped_word = arabic_reshaper.reshape(word_info['word'])
            bidi_word = get_display(reshaped_word)
            btn = MDRaisedButton(text=bidi_word, size_hint=(1, None), height='40dp')
            btn.bind(on_release=lambda btn, word_info=word_info: self.show_word(word_info))
            words_layout.add_widget(btn)

        scroll_view.add_widget(words_layout)
        self.layout.add_widget(scroll_view)

        # Back Button
        button_layout = BoxLayout(size_hint_y=None, height='50dp', padding=10, spacing=10)
        back_button = MDRaisedButton(text='Back', size_hint=(1, None), height='50dp')
        back_button.bind(on_release=self.go_back)
        button_layout.add_widget(back_button)
        
        self.layout.add_widget(button_layout)

    def show_word(self, word_info):
        word_screen = WordScreen(name=word_info['word'], word_info=word_info)
        if not self.manager.has_screen(word_info['word']):
            self.manager.add_widget(word_screen)
        self.manager.current = word_info['word']

    def go_back(self, instance):
        self.manager.current = 'lesson_list'

class LessonListScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=[20, 20, 20, 20], spacing=20)
        self.lesson_scores = {}

        scroll_view = MDScrollView(size_hint=(1, 1), do_scroll_x=False, do_scroll_y=True)
        lesson_layout = MDGridLayout(cols=1, size_hint_y=None, spacing=10, padding=[10, 10, 10, 10])
        lesson_layout.bind(minimum_height=lesson_layout.setter('height'))

        for lesson in lessons.keys():
            reshaped_text = arabic_reshaper.reshape(lesson)
            bidi_text = get_display(reshaped_text)
            btn = MDRaisedButton(text=bidi_text, size_hint=(1, None), height='40dp')
            btn.bind(on_release=lambda btn, lesson_name=lesson: self.show_lesson(lesson_name))
            lesson_layout.add_widget(btn)

        scroll_view.add_widget(lesson_layout)
        layout.add_widget(scroll_view)

        back_button = MDRaisedButton(text='Back', size_hint=(1, None), height='40dp')
        back_button.bind(on_release=self.go_back)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def show_lesson(self, lesson_name):
        lesson_screen = LessonScreen(name=lesson_name, lesson_name=lesson_name)
        self.manager.add_widget(lesson_screen)
        self.manager.current = lesson_name

    def go_back(self, instance):
        self.manager.current = 'main'

class MyWordsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.on_enter()

        for word_info in my_words:
            btn = Button(text=word_info['word'], size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn, word_info=word_info: self.show_word(word_info))
            layout.add_widget(btn)

        back_button = Button(text='Back')
        back_button.bind(on_release=self.go_back)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def show_word(self, word_info):
        word_screen = WordScreen(name=word_info['word'], word_info=word_info)
        self.manager.add_widget(word_screen)
        self.manager.current = word_info['word']

    def on_enter(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical')

        scroll_view=ScrollView(size_hint=(1,1) , do_scroll_x=False , do_scroll_y=True)
        words_layout = GridLayout(cols = 1 , size_hint_y=None)
        words_layout.bind(minimum_height = words_layout.setter('height'))


        for word_info in my_words:
            btn = Button(text=word_info['word'], size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn, word_info=word_info: self.show_word(word_info))
            words_layout.add_widget(btn)

        scroll_view.add_widget(words_layout)
        layout.add_widget(scroll_view)

        back_button = Button(text='Back')
        back_button.bind(on_release=self.go_back)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'main' 

class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Main layout
        self.layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)

        # Guide button (top right)
        self.guide_button = MDRaisedButton(
            text="Guide",
            size_hint=(None, None),
            size=(200, 50),
            on_release=self.open_guide
        )
        guide_layout = MDAnchorLayout(anchor_x='right', anchor_y='top')
        guide_layout.add_widget(self.guide_button)

        # Select Lesson button
        self.select_lesson_button = MDRaisedButton(
            text="Select Lesson",
            size_hint=(0.8, None),
            height=50,
            pos_hint={'center_x': 0.5},
            on_release=self.select_lesson
        )

        # Exam button
        self.exam_button = MDRaisedButton(
            text="Exam",
            size_hint=(0.8, None),
            height=50,
            pos_hint={'center_x': 0.5},
            on_release=self.start_exam
        )

        # My Words button
        self.my_words_button = MDRaisedButton(
            text="My Words",
            size_hint=(0.8, None),
            height=50,
            pos_hint={'center_x': 0.5},
            on_release=self.view_my_words
        )

        # Search button (bottom left)
        self.search_button = MDRaisedButton(
            text="Search",
            size_hint=(None, None),
            size=(200, 50),
            on_release=self.search
        )
        search_layout = MDAnchorLayout(anchor_x='left', anchor_y='bottom')
        search_layout.add_widget(self.search_button)

        # Adding buttons to main layout
        self.layout.add_widget(guide_layout)
        self.layout.add_widget(self.select_lesson_button)
        self.layout.add_widget(self.exam_button)
        self.layout.add_widget(self.my_words_button)
        self.layout.add_widget(search_layout)

        self.add_widget(self.layout)

    def on_enter(self, *args):
        # Apply theme colors
        self.guide_button.md_bg_color = MDApp.get_running_app().theme_cls.primary_color
        self.select_lesson_button.md_bg_color = MDApp.get_running_app().theme_cls.primary_color
        self.exam_button.md_bg_color = MDApp.get_running_app().theme_cls.primary_color
        self.my_words_button.md_bg_color = MDApp.get_running_app().theme_cls.primary_color
        self.search_button.md_bg_color = MDApp.get_running_app().theme_cls.primary_color

    def open_guide(self, instance):
        self.manager.current = 'guide'

    def select_lesson(self, instance):
        self.manager.current = 'lesson_list'

    def start_exam(self, instance):
        self.manager.current = 'exam_lesson_list'

    def view_my_words(self, instance):
        self.manager.current = 'my_words'

    def search(self, instance):
        self.manager.current = 'search' 
    
class SearchScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Main layout
        self.layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)

        # Title label
        self.title_label = MDLabel(
            text="Enter Your Word",
            halign="center",
            theme_text_color="Primary",
            font_style="H4"
        )

        # Text input field
        self.search_input = MDTextField(
            hint_text="Type the word here",
            size_hint_x=0.8,
            pos_hint={'center_x': 0.5}
        )

        # Search button
        self.search_button = MDRaisedButton(
            text="Search",
            size_hint=(0.5, None),
            height=50,
            pos_hint={'center_x': 0.5},
            on_release=self.search_word
        )

        # Back button
        self.back_button = MDRaisedButton(
            text="Back",
            size_hint=(0.5, None),
            height=50,
            pos_hint={'center_x': 0.5},
            on_release=self.go_back
        )

        # Adding widgets to layout
        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.search_input)
        self.layout.add_widget(self.search_button)
        self.layout.add_widget(self.back_button)

        self.add_widget(self.layout)

    def on_enter(self, *args):
        # Apply theme colors
        self.search_button.md_bg_color = MDApp.get_running_app().theme_cls.primary_color
        self.back_button.md_bg_color = MDApp.get_running_app().theme_cls.primary_color

    def search_word(self, instance):
        word = self.search_input.text.lower()
        for lesson_name, lesson in lessons.items():
            for word_info in lesson:
                if word_info['word'] == word:
                    word_screen = WordScreen(name=word_info['word'], word_info=word_info)
                    self.manager.add_widget(word_screen)
                    self.manager.current = word_info['word']
                    return
        else:
            print("Word not found.")

    def go_back(self, instance):
        self.manager.current = 'main'

class VocabularyApp(MDApp):
    def build(self):
        sm = ScreenManager()
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        sm.add_widget(EnterNameScreen(name='enter_name'))
        sm.add_widget(EnterAgeScreen(name='enter_age'))
        sm.add_widget(EnterEmailScreen(name='enter_email'))
        sm.add_widget(GuideScreen(name='guide'))
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(LessonListScreen(name='lesson_list'))
        sm.add_widget(SearchScreen(name='search'))
        sm.add_widget(MyWordsScreen(name='my_words'))
        sm.add_widget(ExamLessonListScreen(name='exam_lesson_list'))
        
        return sm
    
class ExamScreen(MDScreen):
    def __init__(self, lesson_name, **kwargs):
        super().__init__(**kwargs)
        self.lesson_name = lesson_name
        self.words = sample(lessons[lesson_name], 12)
        self.current_index = 0
        self.score = 0
        self.layout = MDBoxLayout(orientation='vertical', padding=[20, 20, 20, 20], spacing=20)
        self.add_widget(self.layout)
        self.show_question()

    def show_question(self):
        self.layout.clear_widgets()
        if self.current_index < len(self.words):
            word_info = self.words[self.current_index]
            question_label = MDLabel(text=f"{word_info['word']}", font_style='H5', halign='center', size_hint_y=None, height='40dp')
            self.layout.add_widget(question_label)

            correct_meaning = word_info['meaning']
            all_meanings = [w['meaning'] for w in lessons[self.lesson_name] if w != word_info]

            options = {correct_meaning}
            while len(options) < 4:
                options.add(choice(all_meanings))
            options = list(options)
            shuffle(options)

            self.correct_button = None
            for option in options:
                reshaped_text = arabic_reshaper.reshape(option)
                bidi_text = get_display(reshaped_text)
                btn = MDRaisedButton(text=bidi_text, halign='center', font_name='B-NAZANIN.ttf',size_hint=(1, None), height='40dp')
                if option == correct_meaning:
                    self.correct_button = btn
                btn.bind(on_release=lambda btn, correct=option == correct_meaning: self.check_answer(btn, correct))
                self.layout.add_widget(btn)
        else:
            score_label = MDLabel(text=f'Your score: {self.score}/12', font_style='H5', halign='center', size_hint_y=None, height='40dp')
            self.layout.add_widget(score_label)
            exit_button = MDRaisedButton(text='Exit', size_hint=(1, None), height='40dp')
            exit_button.bind(on_release=self.exit_exam)
            self.layout.add_widget(exit_button)

    def check_answer(self, btn, correct):
        if correct:
            btn.md_bg_color = (0, 1, 0, 1)
            self.score += 1
        else:
            btn.md_bg_color = (1, 0, 0, 1)
            self.correct_button.md_bg_color = (0, 1, 0, 1)

        self.current_index += 1
        Clock.schedule_once(lambda dt: self.show_question(), 1)

    def exit_exam(self, instance):
        self.manager.current = 'main'

class ExamLessonListScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation='vertical', padding=[20, 20, 20, 20], spacing=20)
        self.lesson_scores = {}

        scroll_view = MDScrollView(size_hint=(1, 1), do_scroll_x=False, do_scroll_y=True)
        lesson_layout = MDGridLayout(cols=1, size_hint_y=None, spacing=10, padding=[10, 10, 10, 10])
        lesson_layout.bind(minimum_height=lesson_layout.setter('height'))

        for lesson in lessons.keys():
            reshaped_text = arabic_reshaper.reshape(lesson)
            bidi_text = get_display(reshaped_text)
            btn = MDRaisedButton(text=bidi_text, size_hint=(1, None), height='40dp')
            btn.bind(on_release=lambda btn, lesson_name=lesson: self.show_exam(lesson_name))
            lesson_layout.add_widget(btn)

        scroll_view.add_widget(lesson_layout)
        layout.add_widget(scroll_view)

        back_button = MDRaisedButton(text='Back', size_hint=(1, None), height='40dp')
        back_button.bind(on_release=self.go_back)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def show_exam(self, lesson_name):
        exam_screen = ExamScreen(name=f'exam_{lesson_name}', lesson_name=lesson_name)
        self.manager.add_widget(exam_screen)
        self.manager.current = f'exam_{lesson_name}'

    def update_lesson_colors(self):
        for button in self.children[0].children:
            lesson_name = button.text
            if lesson_name in self.lesson_scores:
                score = self.lesson_scores[lesson_name]
                if score == 12:
                    button.md_bg_color = (0, 1, 0, 1)
                elif score >= 6:
                    button.md_bg_color = (1, 0.5, 0, 1)
                else:
                    button.md_bg_color = (1, 0, 0, 1)
            else:
                button.md_bg_color = (1, 1, 1, 1)

    def go_back(self, instance):
        self.update_lesson_colors()
        self.manager.current = 'main'

if __name__ == '__main__':
    VocabularyApp().run()