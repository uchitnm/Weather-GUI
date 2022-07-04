################## ~Basic Weather APP~ ################## 
#                Programed by: Uchit N M                #
#                  Mentor: Sumanth L                    #
######################################################### 


from tkinter import *
from tkinter import ttk

import requests
from time import *
from tkinter import messagebox

# Before Using -
# 1.Sign in to 'http://openweathermap.org' to get the API Key/ID.
# 2.Install requests module (use pip (pip3 : Mac OS X) install requests for windows)



def time():
    global label1, label
    time_=strftime('%H:%M:%S %p')
    day=strftime('%d-%B-%Y  %a ')
    label.config(text=time_)
    label1.config(text=day)
    label.after(1000,time)




root=Tk()
root.title('::Weather::')
# root.geometry('900x900')
root.resizable(0,0)

def about():
    messagebox.showinfo(" Credits", "Developed by Uchit N M\nMentor: Sumanth L")

your_API_ID = 'API_KEY'


def change_label(var_name,value_new):
    var_name.config(text = value_new)

def app():
    global e 
    global label 
    global label1
    pin=e.get()
    # print(pin)
    try:
        local_weather=f'http://api.openweathermap.org/data/2.5/weather?zip={pin},in&units=metric&appid={your_API_ID}'

        request_object = requests.get(local_weather)

        data = request_object.json()
        
        b.grid(row=3,column=3)

        PIN.destroy()
        # e.destroy()
        # b.destroy()
        label=Label(root,font=('ds-digital',50),foreground='navy blue')
        label.grid(column=3,row=4)
        label1=Label(root,font=('ds-digital',20),foreground='navy blue')
        label1.grid(column=3,row=5)
        time()

        def temperature():
            main=data['main']
            temp=str(main['temp'])
            min_t=str(main['temp_min'])
            max_t=str(main['temp_max'])
            n=Label(root,text='```````CURRENT UPDATES```````',font=('monaco 16 bold'),fg='red')
            n.grid(row=2,column=2)
            t_d=Label(root,text='-----------------------------------------')
            t_d.grid(row=3,column=2)
            t_h=Label(root,text=':::::::::: CURRENT TEMPERATURE ::::::::::',font=('monaco 14 bold'),fg='brown')
            t_h.grid(row=4,column=2)
            temp_lable=Label(root,text='Current Temp: '+ temp,font=('monaco 13'))
            temp_lable.grid(row=5,column=2)
            min_temp_lable=Label(root,text='Minimum Temp: '+ min_t,font=('monaco 13'))
            min_temp_lable.grid(row=6,column=2)
            max_temp_lable=Label(root,text='Maximum Temp: '+ max_t,font=('monaco 13'))
            max_temp_lable.grid(row=7,column=2)
        temperature()
        def pressure_humidity():
            main=data['main']
            p=main['pressure']
            h=main['humidity']
            p_h=Label(root,text= '::::::::::: PRESSURE & HUMIDITY :::::::::::',font=('monaco 14 bold'),fg='brown')
            p_h.grid(row=8,column=2)
            pree=Label(root,text='Pressure: '+ str(p)+' hPa',font=('monaco 13'))
            pree.grid(row=9,column=2)
            hu=Label(root,text='Humidity: '+ str(h)+'%',font=('monaco 13'))
            hu.grid(row=10,column=2)
        pressure_humidity()
        def cloud():
            c=data['weather']
            c=c[0]
            c_t=c['main']
            c_d=c['description']
            c_p=data['clouds']
            c_p=c_p['all']
            p_h=Label(root,text= '::::::::::::::::: CLOUD INFO :::::::::::::::',font=('monaco 14 bold'),fg='brown')
            p_h.grid(row=11,column=2)
            pree=Label(root,text='Clouds: '+ str(c_t)+'.',font=('monaco 13'))
            pree.grid(row=13,column=2)
            hu=Label(root,text='Description: '+ str(c_d)+'.',font=('monaco 13'))
            hu.grid(row=13,column=2)
            hu=Label(root,text='Coverage: '+ str(c_p)+'%',font=('monaco 13'))
            hu.grid(row=14,column=2)
        cloud()
        def wind_info():
            main=data['wind']
            speed=main['speed']
            # deg=main['deg']
            # gust=main['gust']
            # print(':::::::::: WIND ::::::::::')
            # print(' Wind speed: %a m/s'%speed)
            # print('Wind Direction: %a'%deg)
            # print(' Wind Gust: %a m/s'%gust)
            p_h=Label(root,text= '::::::::::::::::::: WIND ::::::::::::::::::::',font=('monaco 14 bold'),fg='brown')
            p_h.grid(row=15,column=2)
            pree=Label(root,text='Speed: '+ str(speed)+' m/s',font=('monaco 13'))
            pree.grid(row=16,column=2)
        wind_info()
        def visibility():
            vis=data['visibility']
            t_h=Label(root,text='::::::::::::::::: VISIBILITY ::::::::::::::::',font=('monaco 14 bold'),fg='brown')
            t_h.grid(row=17,column=2)
            temp_lable=Label(root,text='Visibility: '+ str(vis),font=('monaco 13'))
            temp_lable.grid(row=18,column=2)
        visibility()
        def location():
            nonlocal pin
            global d_lable
            main=data['coord']
            lon=main['lon']
            lat=main['lat']
            timezone=data['timezone']
            name=data['name']
            h=Label(root,text='::::::::::::::: LOCATION INFO :::::::::::::::',font=('monaco 14 bold'),fg='brown')
            h.grid(row=19,column=2)
            a=Label(root,text='Longitude: '+ str(lon),font=('monaco 13'))
            a.grid(row=20,column=2)
            b_lable=Label(root,text='Latitude: '+ str(lat),font=('monaco 13'))
            b_lable.grid(row=21,column=2)
            c_lable=Label(root,text='Timezone: '+ str(timezone),font=('monaco 13'))
            c_lable.grid(row=22,column=2)
            try :
                change_label(var_name=d_lable,value_new='')
            except Exception:
                pass
            d_lable=Label(root,text='Region: '+ str(name),font=('monaco 13'))
            d_lable.grid(row=23,column=2)
            e_lable=Label(root,text='PIN code: '+ str(pin),font=('monaco 13'))
            e_lable.grid(row=24,column=2)
            t_d=Label(root,text='-----------------------------------------')
            t_d.grid(row=25,column=2)

        location()
    except KeyError:
        if pin=='':
            messagebox.showerror('NO Input','No PIN Code given!!')
        elif len(pin)>6:
            messagebox.showerror('Invalid PIN Code','Invalid PIN Code\nNo.of digits,Exceding the limit.')
        elif len(pin)<6:
            messagebox.showerror('Invalid PIN Code','Invalid PIN Code\nNo.of digits,Below the limit.')
        else:
            messagebox.showerror('Invalid PIN Code','Invalid PIN Code.\nPIN Code NOT Found!')



bar = Menu(root)
about_menu = Menu(bar, tearoff=0)
about_menu.add_command(label="Credits", command=about)
about_menu.add_separator()
about_menu.add_command(label="Exit", command=exit)
bar.add_cascade(label="About", menu=about_menu)
root.config(menu=bar)


PIN=Label(root,text='Enter the PIN Code: ',font=('monaco 16 '),fg='navy blue',bg='MintCream')
PIN.grid(row=2,column=2)
e=ttk.Entry(root)
e.grid(row=2,column=3)

b=Button(text='Press to Search.',font=('monaco 16 '))

b.grid(row=2,column=4)
b.configure(command=app,fg='navy blue')
root.configure(bg='MintCream')
# root.bind('<Return>',app)

root.mainloop()
