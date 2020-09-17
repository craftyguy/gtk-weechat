from gi.repository import Gtk, Handy


class GtkWeechatLeaflet(Handy.Leaflet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_interpolate_size(True)
        self.set_transition_type(Handy.LeafletTransitionType.SLIDE)

        self.buflist_page = Gtk.Box(orientation='horizontal')
        self.chat_page = Gtk.Box(orientation='horizontal')
        self.main_page = Gtk.Box(orientation='vertical')

        self.add(self.buflist_page)
        self.add(self.main_page)

    def toggle_visible(self, *args):
        if self.get_visible_child() == self.buflist_page:
            self.set_visible_child(self.main_page)
        else:
            self.set_visible_child(self.buflist_page)

    def set_visible(self, page, *args):
        if page == 'buflist':
            self.set_visible_child(self.buflist_page)
        elif page == 'main':
            self.set_visible_child(self.main_page)
        else:
            print('ERROR: Unknown page requested')
