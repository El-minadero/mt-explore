from view.view_base import ViewContract
from model.model import DatabaseModel


class ControllerInterface:


    def __init__(self,controller):
        self.controller = controller

    def create_help_menu_string(self,title,functionality):
        separator='***************************\n'

        header  = separator + title + '\n' + separator
        actions = ""
        for key, value in functionality.items():
            actions=actions + '\t' + key + ":" + "\t\t" + value + '\n'

        total = header + actions

        print(total)

    def connect_view(self,view: ViewContract):
        self._connect_view(view)
        self.controller.connect_view(view)

    def connect_model(self,model: DatabaseModel):
        self._connect_model(model)
        self.controller.connect_model(model)

    def update_map(self):
        self._update_map()
        self.controller.update_map()

    def update_em(self):
        self._update_em()
        self.controller.update_em()

    def button_press_event(self,event):
        self._button_press_event(event)
        self.controller.button_press_event(event)

    def button_release_event(self,event):
        self._button_release_event(event)
        self.controller.button_release_event(event)

    def key_press_event(self,event):
        self._key_press_event(event)
        self.controller.key_press_event(event)

    def update(self):
        self._update()
        self.controller.update()

    def _connect_view(self, view: ViewContract):
        self.view = view

    def _connect_model(self, model: DatabaseModel):
        self.model = model

    def _update(self):
        pass

    def _update_map(self):
        pass

    def _update_em(self):
        pass

    def _key_press_event(self,event):
        pass

    def _button_press_event(self, event):
        pass

    def _button_release_event(self, event):
        pass


class ControllerBase(ControllerInterface):

    def __init__(self,*args,**kwargs):
        super().__init__(None)

    def connect_view(self, view: ViewContract):
        pass

    def connect_model(self, model: DatabaseModel):
        pass

    def button_press_event(self, event):
        pass
    
    def button_release_event(self,event):
        pass

    def update_map(self):
        pass

    def update_em(self):
        pass

    def update(self):
        pass

    def key_press_event(self, event):
        pass