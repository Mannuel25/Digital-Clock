import tkinter
import tkinter.messagebox
import time


class CountdownTimer:
    def __init__(self):
        self.main_window = tkinter.Tk()
        # set the geometry
        self.main_window.geometry('500x250')
        self.main_window.resizable(width=False,height=False)

        # make frames
        self.top_frame = tkinter.Frame(self.main_window).pack()
        self.mid_frame = tkinter.Frame(self.main_window).pack()
        self.bottom_frame = tkinter.Frame(self.main_window).pack()

        # make widget in top frame
        self.get_secs = tkinter.Label(self.top_frame,
            text='Number of seconds')
        self.get_secs.place(x=110,y=15)
        self.get_secs_entry = tkinter.Entry(self.top_frame, width=10)
        self.get_secs_entry.place(x=225,y=15)

        # widget in mid frame
        self.timer= tkinter.Label(self.mid_frame,text='00:00:00',
           font=('Arial', 59))
        self.timer.place(x=99,y=60)

        # button in bottom frame
        self.start_button = tkinter.Button(self.bottom_frame,text='Start',
            command=self.start)
        self.start_button.place(x=125,y=170)
        self.pause_button = tkinter.Button(self.bottom_frame,
            text='Pause', command = self.pause)
        self.pause_button.place(x=164,y=170)
        self.reset_button = tkinter.Button(self.bottom_frame,
            text='Reset', command = self.reset)
        self.reset_button.place(x=240,y=170)
        self.quit_button = tkinter.Button(self.bottom_frame,
            text='Quit', command = self.main_window.destroy)
        self.quit_button.place(x=356,y=170)

        # enter loop
        tkinter.mainloop()

    def start(self):
        self.state = True
        self.begin_timer()
    
    def pause(self):
        self.state = False
    
    def reset(self):
        self.state = False
        self.timer.config(text='00:00:00',font=('Arial', 59))
   
    def begin_timer(self):
        # get the number of seconds 
        secs = int(self.get_secs_entry.get())
        for no_of_secs in range(secs,-1,-1):
            if self.state == True and no_of_secs < 60:
                # calculate the number of hours, minutes and seconds
                hrs = no_of_secs // 3600
                mins = no_of_secs // 60
                secs = no_of_secs % 60
                # format the hours, minutes
                # and seconds to be displayed
                display_format = '%02d:%02d:%02d' %(hrs, mins, secs)
                self.timer.config(text=display_format)
                # update the mid frame after 
                # decrementing the number of seconds
                self.timer.update()
                time.sleep(1)
                # decrement the number of seconds by one
            elif self.state == True and 60 <= no_of_secs < 3600:
                # calculate the number of hours, minutes and seconds
                hrs = no_of_secs // 3600
                mins = no_of_secs // 60
                secs = no_of_secs % 60
                # format the hours, minutes
                # and seconds to be displayed
                display_format = '%02d:%02d:%02d' %(hrs, mins, secs)
                self.timer.config(text=display_format)
                # update the mid frame after 
                # decrementing the number of seconds
                self.timer.update()
                time.sleep(1)
                # decrement the number of seconds by one
            elif  self.state == True and 3600 <= no_of_secs <= 86400:
                # calculate the number of hours, minutes and seconds
                hrs = no_of_secs // 3600
                mins = (no_of_secs % 3600) // 60
                secs = (no_of_secs % 3600) % 60
                display_format = '%02d:%02d:%02d' %(hrs, mins, secs)
                self.timer.config(text=display_format)
                # update the mid frame after 
                # decrementing the number of seconds
                self.timer.update()
                time.sleep(1)
            
    
yy = CountdownTimer()















Africa/Abidjan
Africa/Accra
Africa/Addis_Ababa
Africa/Algiers
Africa/Asmara
Africa/Bamako
Africa/Bangui
Africa/Banjul
Africa/Bissau
Africa/Blantyre
Africa/Brazzaville
Africa/Bujumbura
Africa/Cairo
Africa/Casablanca
Africa/Ceuta
Africa/Conakry
Africa/Dakar
Africa/Dar_es_Salaam
Africa/Djibouti
Africa/Douala
Africa/El_Aaiun
Africa/Freetown
Africa/Gaborone
Africa/Harare
Africa/Johannesburg
Africa/Juba
Africa/Kampala
Africa/Khartoum
Africa/Kigali
Africa/Kinshasa
Africa/Lagos
Africa/Libreville
Africa/Lome
Africa/Luanda
Africa/Lubumbashi
Africa/Lusaka
Africa/Malabo
Africa/Maputo
Africa/Maseru
Africa/Mbabane
Africa/Mogadishu
Africa/Monrovia
Africa/Nairobi
Africa/Ndjamena
Africa/Niamey
Africa/Nouakchott
Africa/Ouagadougou
Africa/Porto-Novo
Africa/Sao_Tome
Africa/Tripoli
Africa/Tunis
Africa/Windhoek
America/Adak
America/Anchorage
America/Anguilla
America/Antigua
America/Araguaina
America/Argentina/Buenos_Aires
America/Argentina/Catamarca
America/Argentina/Cordoba
America/Argentina/Jujuy
America/Argentina/La_Rioja
America/Argentina/Mendoza
America/Argentina/Rio_Gallegos
America/Argentina/Salta
America/Argentina/San_Juan
America/Argentina/San_Luis
America/Argentina/Tucuman
America/Argentina/Ushuaia
America/Aruba
America/Asuncion
America/Atikokan
America/Bahia
America/Bahia_Banderas
America/Barbados
America/Belem
America/Belize
America/Blanc-Sablon
America/Boa_Vista
America/Bogota
America/Boise
America/Cambridge_Bay
America/Campo_Grande
America/Cancun
America/Caracas
America/Cayenne
America/Cayman
America/Chicago
America/Chihuahua
America/Costa_Rica
America/Creston
America/Cuiaba
America/Curacao
America/Danmarkshavn
America/Dawson
America/Dawson_Creek
America/Denver
America/Detroit
America/Dominica
America/Edmonton
America/Eirunepe
America/El_Salvador
America/Fort_Nelson
America/Fortaleza
America/Glace_Bay
America/Goose_Bay
America/Grand_Turk
America/Grenada
America/Guadeloupe
America/Guatemala
America/Guayaquil
America/Guyana
America/Halifax
America/Havana
America/Hermosillo
America/Indiana/Indianapolis
America/Indiana/Knox
America/Indiana/Marengo
America/Indiana/Petersburg
America/Indiana/Tell_City
America/Indiana/Vevay
America/Indiana/Vincennes
America/Indiana/Winamac
America/Inuvik
America/Iqaluit
America/Jamaica
America/Juneau
America/Kentucky/Louisville
America/Kentucky/Monticello
America/Kralendijk
America/La_Paz
America/Lima
America/Los_Angeles
America/Lower_Princes
America/Maceio
America/Managua
America/Manaus
America/Marigot
America/Martinique
America/Matamoros
America/Mazatlan
America/Menominee
America/Merida
America/Metlakatla
America/Mexico_City
America/Miquelon
America/Moncton
America/Monterrey
America/Montevideo
America/Montserrat
America/Nassau
America/New_York
America/Nipigon
America/Nome
America/Noronha
America/North_Dakota/Beulah
America/North_Dakota/Center
America/North_Dakota/New_Salem
America/Nuuk
America/Ojinaga
America/Panama
America/Pangnirtung
America/Paramaribo
America/Phoenix
America/Port-au-Prince
America/Port_of_Spain
America/Porto_Velho
America/Puerto_Rico
America/Punta_Arenas
America/Rainy_River
America/Rankin_Inlet
America/Recife
America/Regina
America/Resolute
America/Rio_Branco
America/Santarem
America/Santiago
America/Santo_Domingo
America/Sao_Paulo
America/Scoresbysund
America/Sitka
America/St_Barthelemy
America/St_Johns
America/St_Kitts
America/St_Lucia
America/St_Thomas
America/St_Vincent
America/Swift_Current
America/Tegucigalpa
America/Thule
America/Thunder_Bay
America/Tijuana
America/Toronto
America/Tortola
America/Vancouver
America/Whitehorse
America/Winnipeg
America/Yakutat
America/Yellowknife
Antarctica/Casey
Antarctica/Davis
Anta
Asia/Dushanbe
Asia/Famagusta
Asia/Gaza
Asia/Hebron
Asia/Ho_Chi_Minh
Asia/
['Africa', 'Asmara']
['Africa', 'Bamako']
['Africa', 'Bangui']
['Africa', 'Banjul']
['Africa', 'Bissau']
['Africa', 'Blantyre']
['Africa', 'Brazzaville']
['Africa', 'Bujumbura']
['Africa', 'Cairo']
['Africa', 'Casablanca']
['Africa', 'Ceuta']
['Africa', 'Conakry']
['Africa', 'Dakar']
['Africa', 'Dar_es_Salaam']
['Africa', 'Djibouti']
['Africa', 'Douala']
['Africa', 'El_Aaiun']
['Africa', 'Freetown']
['Africa', 'Gaborone']
['Africa', 'Harare']
['Africa', 'Johannesburg']
['Africa', 'Juba']
['Africa', 'Kampala']
['Africa', 'Khartoum']
['Africa', 'Kigali']
['Africa', 'Kinshasa']
['Africa', 'Lagos']
['Africa', 'Libreville']
['Africa', 'Lome']
['Africa', 'Luanda']
['Africa', 'Lubumbashi']
['Africa', 'Lusaka']
['Africa', 'Malabo']
['Africa', 'Maputo']
['Africa', 'Maseru']
['Africa', 'Mbabane']
['Africa', 'Mogadishu']
['Africa', 'Monrovia']
['Africa', 'Nairobi']
['Africa', 'Ndjamena']
['Africa', 'Niamey']
['Africa', 'Nouakchott']
['Africa', 'Ouagadougou']
['Africa', 'Porto-Novo']
['Africa', 'Sao_Tome']
['Africa', 'Tripoli']
['Africa', 'Tunis']
['Africa', 'Windhoek']
['America', 'Adak']
['America', 'Anchorage']
['America', 'Anguilla']
['America', 'Antigua']
['America', 'Araguaina']
['America', 'Argentina', 'Buenos_Aires']
['America', 'Argentina', 'Catamarca']
['America', 'Argentina', 'Cordoba']
['America', 'Argentina', 'Jujuy']
['America', 'Argentina', 'La_Rioja']
['America', 'Argentina', 'Mendoza']
['America', 'Argentina', 'Rio_Gallegos']
['America', 'Argentina', 'Salta']
['America', 'Argentina', 'San_Juan']
['America', 'Argentina', 'San_Luis']
['America', 'Argentina', 'Tucuman']
['America', 'Argentina', 'Ushuaia']
['America', 'Aruba']
['America', 'Asuncion']
['America', 'Atikokan']
['America', 'Bahia']
['America', 'Bahia_Banderas']
['America', 'Barbados']
['America', 'Belem']
['America', 'Belize']
['America', 'Blanc-Sablon']
['America', 'Boa_Vista']
['America', 'Bogota']
['America', 'Boise']
['America', 'Cambridge_Bay']
['America', 'Campo_Grande']
['America', 'Cancun']
['America', 'Caracas']
['America', 'Cayenne']
['America', 'Cayman']
['America', 'Chicago']
['America', 'Chihuahua']
['America', 'Costa_Rica']
['America', 'Creston']
['America', 'Cuiaba']
['America', 'Curacao']
['America', 'Danmarkshavn']
['America', 'Dawson']
['America', 'Dawson_Creek']
['America', 'Denver']
['America', 'Detroit']
['America', 'Dominica']
['America', 'Edmonton']
['America', 'Eirunepe']
['America', 'El_Salvador']
['America', 'Fort_Nelson']
['America', 'Fortaleza']
['America', 'Glace_Bay']
['America', 'Goose_Bay']
['America', 'Grand_Turk']
['America', 'Grenada']
['America', 'Guadeloupe']
['America', 'Guatemala']
['America', 'Guayaquil']
['America', 'Guyana']
['America', 'Halifax']
['America', 'Havana']
['America', 'Hermosillo']
['America', 'Indiana', 'Indianapolis']
['America', 'Indiana', 'Knox']
['America', 'Indiana', 'Marengo']
['America', 'Indiana', 'Petersburg']
['America', 'Indiana', 'Tell_City']
['America', 'Indiana', 'Vevay']
['America', 'Indiana', 'Vincennes']
['America', 'Indiana', 'Winamac']
['America', 'Inuvik']
['America', 'Iqaluit']
['America', 'Jamaica']
['America', 'Juneau']
['America', 'Kentucky', 'Louisville']
['America', 'Kentucky', 'Monticello']
['America', 'Kralendijk']
['America', 'La_Paz']
['America', 'Lima']
['America', 'Los_Angeles']
['America', 'Lower_Princes']
['America', 'Maceio']
['America', 'Managua']
['America', 'Manaus']
['America', 'Marigot']
['America', 'Martinique']
['America', 'Matamoros']
['America', 'Mazatlan']
['America', 'Menominee']
['America', 'Merida']
['America', 'Metlakatla']
['America', 'Mexico_City']
['America', 'Miquelon']
['America', 'Moncton']
['America', 'Monterrey']
['America', 'Montevideo']
['America', 'Montserrat']
['America', 'Nassau']
['America', 'New_York']
['America', 'Nipigon']
['America', 'Nome']
['America', 'Noronha']
['America', 'North_Dakota', 'Beulah']
['America', 'North_Dakota', 'Center']
['America', 'North_Dakota', 'New_Salem']
['America', 'Nuuk']
['America', 'Ojinaga']
['America', 'Panama']
['America', 'Pangnirtung']
['America', 'Paramaribo']
['America', 'Phoenix']
['America', 'Port-au-Prince']
['America', 'Port_of_Spain']
['America', 'Porto_Velho']
['America', 'Puerto_Rico']
['America', 'Punta_Arenas']
['America', 'Rainy_River']
['America', 'Rankin_Inlet']
['America', 'Recife']
['America', 'Regina']
['America', 'Resolute']
['America', 'Rio_Branco']
['America', 'Santarem']
['America', 'Santiago']
['America', 'Santo_Domingo']
['America', 'Sao_Paulo']
['America', 'Scoresbysund']
['America', 'Sitka']
['America', 'St_Barthelemy']
['America', 'St_Johns']
['America', 'St_Kitts']
['America', 'St_Lucia']
['America', 'St_Thomas']
['America', 'St_Vincent']
['America', 'Swift_Current']
['America', 'Tegucigalpa']
['America', 'Thule']
['America', 'Thunder_Bay']
['America', 'Tijuana']
['America', 'Toronto']
['America', 'Tortola']
['America', 'Vancouver']
['America', 'Whitehorse']
['America', 'Winnipeg']
['America', 'Yakutat']
['America', 'Yellowknife']
['Antarctica', 'Casey']
['Antarctica', 'Davis']
['Antarctica', 'DumontDUrville']
['Antarctica', 'Macquarie']
['Antarctica', 'Mawson']
['Antarctica', 'McMurdo']
['Antarctica', 'Palmer']
['Antarctica', 'Rothera']
['Antarctica', 'Syowa']
['Antarctica', 'Troll']
['Antarctica', 'Vostok']
['Arctic', 'Longyearbyen']
['Asia', 'Aden']
['Asia', 'Almaty']
['Asia', 'Amman']
['Asia', 'Anadyr']
['Asia', 'Aqtau']
['Asia', 'Aqtobe']
['Asia', 'Ashgabat']
['Asia', 'Atyrau']
['Asia', 'Baghdad']
['Asia', 'Bahrain']
['Asia', 'Baku']
['Asia', 'Bangkok']
['Asia', 'Barnaul']
['Asia', 'Beirut']
['Asia', 'Bishkek']
['Asia', 'Brunei']
['Asia', 'Chita']
['Asia', 'Choibalsan']
['Asia', 'Colombo']
['Asia', 'Damascus']
['Asia', 'Dhaka']
['Asia', 'Dili']
['Asia', 'Dubai']
['Asia', 'Dushanbe']
['Asia', 'Famagusta']
['Asia', 'Gaza']
['Asia', 'Hebron']
['Asia', 'Ho_Chi_Minh']
['Asia', 'Hong_Kong']
['Asia', 'Hovd']
['Asia', 'Irkutsk']
['Asia', 'Jakarta']
['Asia', 'Jayapura']
['Asia', 'Jerusalem']
['Asia', 'Kabul']
['Asia', 'Kamchatka']
['Asia', 'Karachi']
['Asia', 'Kathmandu']
['Asia', 'Khandyga']
['Asia', 'Kolkata']
['Asia', 'Krasnoyarsk']
['Asia', 'Kuala_Lumpur']
['Asia', 'Kuching']
['Asia', 'Kuwait']
['Asia', 'Macau']
['Asia', 'Magadan']
['Asia', 'Makassar']
['Asia', 'Manila']
['Asia', 'Muscat']
['Asia', 'Nicosia']
['Asia', 'Novokuznetsk']
['Asia', 'Novosibirsk']
['Asia', 'Omsk']
['Asia', 'Oral']
['Asia', 'Phnom_Penh']
['Asia', 'Pontianak']
['Asia', 'Pyongyang']
['Asia', 'Qatar']
['Asia', 'Qostanay']
['Asia', 'Qyzylorda']
['Asia', 'Riyadh']
['Asia', 'Sakhalin']
['Asia', 'Samarkand']
['Asia', 'Seoul']
['Asia', 'Shanghai']
['Asia', 'Singapore']
['Asia', 'Srednekolymsk']
['Asia', 'Taipei']
['Asia', 'Tashkent']
['Asia', 'Tbilisi']
['Asia', 'Tehran']
['Asia', 'Thimphu']
['Asia', 'Tokyo']
['Asia', 'Tomsk']
['Asia', 'Ulaanbaatar']
['Asia', 'Urumqi']
['Asia', 'Ust-Nera']
['Asia', 'Vientiane']
['Asia', 'Vladivostok']
['Asia', 'Yakutsk']
['Asia', 'Yangon']
['Asia', 'Yekaterinburg']
['Asia', 'Yerevan']
['Atlantic', 'Azores']
['Atlantic', 'Bermuda']
['Atlantic', 'Canary']
['Atlantic', 'Cape_Verde']
['Atlantic', 'Faroe']
['Atlantic', 'Madeira']
['Atlantic', 'Reykjavik']
['Atlantic', 'South_Georgia']
['Atlantic', 'St_Helena']
['Atlantic', 'Stanley']
['Australia', 'Adelaide']
['Australia', 'Brisbane']
['Australia', 'Broken_Hill']
['Australia', 'Darwin']
['Australia', 'Eucla']
['Australia', 'Hobart']
['Australia', 'Lindeman']
['Australia', 'Lord_Howe']
['Australia', 'Melbourne']
['Australia', 'Perth']
['Australia', 'Sydney']
['Canada', 'Atlantic']
['Canada', 'Central']
['Canada', 'Eastern']
['Canada', 'Mountain']
['Canada', 'Newfoundland']
['Canada', 'Pacific']
['Europe', 'Amsterdam']
['Europe', 'Andorra']
['Europe', 'Astrakhan']
['Europe', 'Athens']
['Europe', 'Belgrade']
['Europe', 'Berlin']
['Europe', 'Bratislava']
['Europe', 'Brussels']
['Europe', 'Bucharest']
['Europe', 'Budapest']
['Europe', 'Busingen']
['Europe', 'Chisinau']
['Europe', 'Copenhagen']
['Europe', 'Dublin']
['Europe', 'Gibraltar']
['Europe', 'Guernsey']
['Europe', 'Helsinki']
['Europe', 'Isle_of_Man']
['Europe', 'Istanbul']
['Europe', 'Jersey']
['Europe', 'Kaliningrad']
['Europe', 'Kiev']
['Europe', 'Kirov']
['Europe', 'Lisbon']
['Europe', 'Ljubljana']
['Europe', 'London']
['Europe', 'Luxembourg']
['Europe', 'Madrid']
['Europe', 'Malta']
['Europe', 'Mariehamn']
['Europe', 'Minsk']
['Europe', 'Monaco']
['Europe', 'Moscow']
['Europe', 'Oslo']
['Europe', 'Paris']
['Europe', 'Podgorica']
['Europe', 'Prague']
['Europe', 'Riga']
['Europe', 'Rome']
['Europe', 'Samara']
['Europe', 'San_Marino']
['Europe', 'Sarajevo']
['Europe', 'Saratov']
['Europe', 'Simferopol']
['Europe', 'Skopje']
['Europe', 'Sofia']
['Europe', 'Stockholm']
['Europe', 'Tallinn']
['Europe', 'Tirane']
['Europe', 'Ulyanovsk']
['Europe', 'Uzhgorod']
['Europe', 'Vaduz']
['Europe', 'Vatican']
['Europe', 'Vienna']
['Europe', 'Vilnius']
['Europe', 'Volgograd']
['Europe', 'Warsaw']
['Europe', 'Zagreb']
['Europe', 'Zaporozhye']
['Europe', 'Zurich']
['Indian', 'Antananarivo']
['Indian', 'Chagos']
['Indian', 'Christmas']
['Indian', 'Cocos']
['Indian', 'Comoro']
['Indian', 'Kerguelen']
['Indian', 'Mahe']
['Indian', 'Maldives']
['Indian', 'Mauritius']
['Indian', 'Mayotte']
['Indian', 'Reunion']
['Pacific', 'Apia']
['Pacific', 'Auckland']
['Pacific', 'Bougainville']
['Pacific', 'Chatham']
['Pacific', 'Chuuk']
['Pacific', 'Easter']
['Pacific', 'Efate']
['Pacific', 'Enderbury']
['Pacific', 'Fakaofo']
['Pacific', 'Fiji']
['Pacific', 'Funafuti']
['Pacific', 'Galapagos']
['Pacific', 'Gambier']
['Pacific', 'Guadalcanal']
['Pacific', 'Guam']
['Pacific', 'Honolulu']
['Pacific', 'Kiritimati']
['Pacific', 'Kosrae']
['Pacific', 'Kwajalein']
['Pacific', 'Majuro']
['Pacific', 'Marquesas']
['Pacific', 'Midway']
['Pacific', 'Nauru']
['Pacific', 'Niue']
['Pacific', 'Norfolk']
['Pacific', 'Noumea']
['Pacific', 'Pago_Pago']
['Pacific', 'Palau']
['Pacific', 'Pitcairn']
['Pacific', 'Pohnpei']
['Pacific', 'Port_Moresby']
['Pacific', 'Rarotonga']
['Pacific', 'Saipan']
['Pacific', 'Tahiti']
['Pacific', 'Tarawa']
['Pacific', 'Tongatapu']
['Pacific', 'Wake']
['Pacific', 'Wallis']
['US', 'Alaska']
['US', 'Arizona']
['US', 'Central']
['US', 'Eastern']
['US', 'Hawaii']
['US', 'Mountain']
['US', 'Pacific']


datetime_NY = datetime.now(pytz.timezone('UTC'))
print("NY time:", datetime_NY.strftime("%H:%M:%S"))




import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime, date
import pytz

timezones = [i.replace('/',', ') for i in pytz.common_timezones]

class Clock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('My Clock')
        #.resizable(0,0)
        self.geometry('350x340')
        self['bg'] = 'black'
        self.frame_1 = tk.Frame(self,bg='black')
        self.frame_2 = tk.Frame(self)
        self.scrollbar = tk.Scrollbar(self.frame_2, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(self.frame_2, 
            bg='black', fg='white',font=('Courier', 11),
            width= 33, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        # remove underscores from each timezone
        zones = [i.replace('_',' ') for i in timezones]
        self.listbox.insert(0, *zones)
        
        self.listbox.pack(side=tk.LEFT,expand='YES',fill=tk.X)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.time_label = tk.Label(self.frame_1, text=datetime.now().strftime('%H:%M:%S'),
            bg='black', fg='white',font=('Courier', 21))
        self.time_label.pack(padx=2,pady=2)
        self.date_label = tk.Label(self.frame_1,text=self.current_date(),
            bg='black', fg='white',font=('Courier', 16))
        self.date_label.pack(padx=2,pady=2)
        self.frame_1.pack(padx=4,pady=25)
        self.frame_2.place(x=15,y=149)

        # schedule a time update every second
        self.time_label.after(1000, self.update_time)

        self.timezone_button = ttk.Button(self.frame_1, text='Select a timezone',
            command=self.timezones)
        self.timezone_button.pack(padx=4,pady=16)

    def current_time(self):
        time = datetime.now().strftime('%H:%M:%S')
        return time
    
    def current_date(self):
        # get today's date
        today_date, weekday = date.today(), datetime.today().weekday()
        date_display = today_date.strftime('%B %d, %Y')
        weekdays = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,
            'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
        for i, j in weekdays.items():
            if weekday == j:
                return  f'{i} {date_display}'
    
    def update_time(self):
        '''update the time every second'''
        self.time_label.configure(text=self.current_time())

        # schedule another time update
        self.time_label.after(1000, self.update_time)
    
    def timezones(self):
        # open the timezones window
        new_window = DisplayTimezones(self)
        # the grab_set method prevents users from interacting with 
        # the main window until this one is closed
        new_window.grab_set()


class DisplayTimezones(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('My Clock')
        self['bg'] = 'black'
        self.geometry('300x246')
        self.resizable(0,0)
        self.frame = tk.Frame(self, bg='black')
        self.label = tk.Label(self.frame, text='Select a timezone',
            bg='black', fg='white',font=('Times', 14))
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(self.frame, 
            bg='black', fg='white', font=('Helvetica', 11),
            width= 33, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        # remove underscores from each timezone
        zones = [i.replace('_',' ') for i in timezones]
        self.listbox.insert(0, *zones)
        self.pick_btn = ttk.Button(self, text='OK',
            command=self.get_pick)

        
        self.frame.pack()
        self.label.pack()
        self.listbox.pack(side=tk.LEFT,expand='YES',fill=tk.X)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.pick_btn.place(x=100,y=217)

    
    def get_pick(self):
        timezones = [i.replace('/',', ') for i in pytz.common_timezones]
        selection = self.listbox.curselection()
        #print('selection>>',selection)
        #print(*[self.listbox.get(i) for i in selection])
        timezone_index = timezones[int(''.join(map(str,selection)))]
        #print('timezone index >>:', timezone_index)
        # get timezone current time
        timezone_current_time = datetime.now(pytz.timezone(timezone_index.replace(', ', '/')))
        print('The time in', *[self.listbox.get(i) for i in selection], 'is :', \
            timezone_current_time.strftime("%H:%M:%S"))
        
        
    


if __name__ == '__main__':
    app = Clock()
    app.mainloop()

def get_timezone(self):
        timezones = [i.replace('/',', ') for i in pytz.common_timezones]
        selection = self.listbox.curselection()
        #print('selection>>',selection)
        #print(*[self.listbox.get(i) for i in selection])
        timezone_index = timezones[int(''.join(map(str,selection)))]
        #print('timezone index >>:', timezone_index)
        # get timezone current time
        timezone_current_time = datetime.now(pytz.timezone(timezone_index.replace(', ', '/')))
        display_format = timezone_current_time.strftime("%H:%M:%S")
        selected_timezones= [*[self.listbox.get(i) for i in selection], display_format]
        print(f'The time in {selected_timezones[0]}, is {selected_timezones[1]}')
        print('SELECTED TIMEZONES:', selected_timezones)
        self.wait_window()
        return selected_timezones