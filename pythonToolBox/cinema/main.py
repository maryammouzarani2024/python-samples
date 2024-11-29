#GUI
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

Builder.load_file('frontend.kv')


import setup
import seat as st
import accounts



class FirstScreen(Screen):
    def buy(self):
        self.manager.current_screen.ids.result_label.text="Hello"

        seat_number=self.manager.current_screen.ids.seat_no.text
        card_number=self.manager.current_screen.ids.card_no.text
        cvc=self.manager.current_screen.ids.cvc.text
        query_seat=st.Seat(seat_number)
        price=query_seat.check_for_available(seat_number)
        if price:
            card=accounts.Accounts(card_number, cvc)
            if card.update_card(price):
                query_seat.buy()
                name=self.manager.current_screen.ids.holder_name.text
                query_seat.create_pdf(name)    
                self.manager.current_screen.ids.result_label.text="Transaction Completed"
        else:
                self.manager.current_screen.ids.result_label.text="Seat is not available"



class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()
    


MainApp().run()



