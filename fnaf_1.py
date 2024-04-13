#link para probar el juego : https://hub.kodland.org/project/248511


#pgzero
import random
import time
WIDTH = 1050
HEIGHT = 593
FPS = 20
mode = "menu"
mode2 = "nada"

num_cam = "cam1a"
dor = "off"
light = "off"
dor2 = "off"
light2 = "off"
#Fondo,personajes,variables
fondoM = Actor("menu1")
intro = Actor("intro")
titulo= Actor("nombre", (170,200))
Static = Actor("static1")
N_G = Actor("new_game", (170,400))
C = Actor("continue", (170,470))
noche1 = Actor("noche1",  (525,296))
oficina = Actor("oficina1", (525,296))
oficina2 = Actor("oficina(light_left)", (525,296))
oficina3 = Actor("oficina(light_right)", (525,296))
fan = Actor("fan_1" , (574,331))
barra = Actor("barra_camara",(525,570))
mapa = Actor("map", (850,370))
dor_R = Actor("Door_right", (1105,290))
dor_L = Actor("Door_lefT", (-100,290))
Button_D_L = Actor("Button_door_left", (-230,290))
Button_L_L = Actor("Button_light_lefT", (-231,376))
Button_D_R = Actor("Button_door_right", (1250,290))
Button_L_R = Actor("Button_light_Right", (1250,376))
time = 12


cam1a = Actor("cam1aa", (804,220))
cam1b = Actor("cam1b", (783,276))
cam5 = Actor("cam5", (679,303))
cam1c = Actor("cam1c", (752,353))
cam3 = Actor("cam3", (720,451))
cam2a = Actor("cam2a", (804,469))
cam2b = Actor("cam2b", (804,510))
cam7 = Actor("cam7", (1016,305))
cam6 = Actor("cam6", (1007,435))
cam4a = Actor("cam4a", (910,471))
cam4b = Actor("cam4b", (910,512))

show_stage = Actor("show_stage")
dining_area = Actor("Dining_Area")
backstage = Actor("Backstage")
pirates_cove =  Actor("Pirates Cove")
supply_closet = Actor("Supply Closet")
west_hall =  Actor("West_Hall")
w_hall_corner = Actor("W. Hall Corner")
restrooms = Actor("Restrooms")
east_hall =  Actor("East Hall")
e_hall_corner =  Actor("E. Hall Corner")

#jumpscares
jumpscareBonnie =  Actor("jumpscareB1", (525,296))
jumpscareB = "off"
jumpscareChica = Actor("jumpscareC1", (525,296))
jumpscareC = "off"

bonnieIA = "show_stage"
chicaIA = "show_stage"


#menu
def update(dt):
    global mode,mode2,bonnieIA,bIA,habitacion,dor,light,dor2,light2,chicaIA,oficina,oficina2,oficina3,jumpscareB
    global jumpscareB_num,jumpscareC,jumpscareC_num,time
    if mode == "menu":
        fredyM = random.randint(1,100)
        
        if fredyM == 2 or fredyM == 10 or fredyM == 50 or fredyM == 25:
            fondoM.image = "menu2"
            fondoM.image = "menu2"
            
        elif fredyM == 3 or fredyM == 34 or fredyM == 45:
            fondoM.image = "menu3"
            fondoM.image = "menu3"
            
        elif fredyM == 4 or fredyM == 24:
            fondoM.image = "menu4"
           
        else:
            fondoM.image = "menu1"
    #Static
        
    if mode == "menu" or mode2 == "camaras" :  
        StaticM = random.randint(1,8)
            
        if StaticM == 2 :
            Static.image = "static2"
                            
        elif StaticM == 3:
            Static.image = "static3"
                            
        elif StaticM == 4:
            Static.image = "static4"
                            
        elif StaticM == 5:
            Static.image = "static5"
                            
        elif StaticM == 6:
            Static.image = "static6"
                            
        elif StaticM == 7:
            Static.image = "static7"
                            
        elif StaticM == 8:
            Static.image = "static8"
                            
        else:
            Static.image = "static1"
    
    #jumpscareBonnie
        
    if jumpscareB == "on":
        jumpscareB_num = random.randint(1,11)
        if jumpscareB_num == 1:
            jumpscareBonnie.image = "jumpscareB1"
        elif jumpscareB_num == 2:
            jumpscareBonnie.image = "jumpscareB2"
        elif jumpscareB_num == 3:
            jumpscareBonnie.image = "jumpscareB3"
        elif jumpscareB_num == 4:
            jumpscareBonnie.image = "jumpscareB4"
        elif jumpscareB_num == 5:
            jumpscareBonnie.image = "jumpscareB5"
        elif jumpscareB_num == 6:
            jumpscareBonnie.image = "jumpscareB6"
        elif jumpscareB_num == 7:
            jumpscareBonnie.image = "jumpscareB7"
        elif jumpscareB_num == 8:
            jumpscareBonnie.image = "jumpscareB8"
        elif jumpscareB_num == 9:
            jumpscareBonnie.image = "jumpscareB9"
        elif jumpscareB_num == 10:
            jumpscareBonnie.image = "jumpscareB10"
        elif jumpscareB_num == 11:
            jumpscareBonnie.image = "jumpscareB11"
            
        #jumpscareChica
    if jumpscareC == "on":
        jumpscareC_num = random.randint(1,16)
        if jumpscareC_num == 1:
            jumpscareChica.image = "jumpscareC1"
        elif jumpscareC_num == 2:
            jumpscareChica.image = "jumpscareC2"
        elif jumpscareC_num == 3:
            jumpscareChica.image = "jumpscareC3"
        elif jumpscareC_num == 4:
            jumpscareChica.image = "jumpscareC4"
        elif jumpscareC_num == 5:
            jumpscareChica.image = "jumpscareC5"
        elif jumpscareC_num == 6:
            jumpscareChica.image = "jumpscareC6"
        elif jumpscareC_num == 7:
            jumpscareChica.image = "jumpscareC7"
        elif jumpscareC_num == 8:
            jumpscareChica.image = "jumpscareC8"
        elif jumpscareC_num == 9:
            jumpscareChica.image = "jumpscareC9"
        elif jumpscareC_num == 10:
            jumpscareChica.image = "jumpscareC10"
        elif jumpscareC_num == 11:
            jumpscareChica.image = "jumpscareC11"
        elif jumpscareC_num == 12:
            jumpscareChica.image = "jumpscareC12"
        elif jumpscareC_num == 13:
            jumpscareChica.image = "jumpscareC13"
        elif jumpscareC_num == 14:
            jumpscareChica.image = "jumpscareC14"
        elif jumpscareC_num == 15:
            jumpscareChica.image = "jumpscareC15"
        elif jumpscareC_num == 16:
            jumpscareChica.image = "jumpscareC16"
    
    if mode == "noche1":
        if time == 6:
            mode2 = "nada"
            mode = "menu"
    
            
            
            
            
            
    
        
    
            
            
            
        
    #BONNIEIA
    if mode == "noche1":
        if bonnieIA == "show_stage":
            bIA = random.randint(1,100)
            if bIA == 15:
                show_stage.image = "Show Stage(no_bonnie)"
                dining_area.image= "Dining Area(bonnie)"
                bonnieIA = "dining_area"
                
        elif bonnieIA == "dining_area":
            habitacion = random.randint(1,10)
            bIA = random.randint(1,100)
            
            if bIA == 49:
                if habitacion == 1 or habitacion == 5:
                    dining_area.image = "Dining_Area"
                    west_hall.image = "West Hall(bonnie)"
                    bonnieIA = "west_hall"
                else:
                    dining_area.image = "Dining_Area"
                    backstage.image = "Backstage(bonnie)"
                    bonnieIA = "backstage"
        
        elif bonnieIA == "backstage":
            bIA = random.randint(1,100)
            if bIA == 34:
                backstage.image = "Backstage"
                west_hall.image = "West Hall(bonnie)"
                bonnieIA = "west_hall"
        
        elif bonnieIA == "west_hall":
             bIA = random.randint(1,100)
             habitacion = random.randint(1,10)
             if bIA == 83:
                 if habitacion == 1 or habitacion == 5 or habitacion == 7 or habitacion == 3:
                     west_hall.image = "West_Hall"
                     w_hall_corner.image = "W. Hall Corner(bonnie)"
                     bonnieIA = "w_hall_corner"
                 else:
                    west_hall.image = "West_Hall"
                    supply_closet.image = "Supply Closet(bonnie)"
                    bonnieIA = "supply_closet"
        
        elif bonnieIA == "supply_closet":
            bIA = random.randint(1,100)
            if bIA == 83:
                supply_closet.image = "Supply Closet"
                west_hall.image = "West Hall(bonnie)"
                bonnieIA = "west_hall"
        
        elif bonnieIA == "w_hall_corner":
            bIA = random.randint(1,100)
            if bIA == 93:
                w_hall_corner.image = "W. Hall Corner"
                oficina2.image = "oficina(bonnie)"
                bonnieIA = "oficina"
        
        elif bonnieIA == "oficina":
            bIA = random.randint(1,100)
            if bIA == 23:
                if dor == "on":
                    UbiC = random.randint(1,2)
                    if UbiC == 1:
                        bonnieIA = "backstage"
                        oficina2.image = "oficina(light_left)"
                        if time == 12:
                            time = 1
                        elif time >= 1:
                            time += 1
                    elif UbiC == 2:
                        bonnieIA = "supply_closet"
                        oficina2.image = "oficina(light_left)"
                        if time == 12:
                            time = 1
                        elif time >= 1:
                            time += 1
                elif dor == "off":
                    
                    if mode2 == "camaras":
                        jumpscareB = "on"
                    
                    
                
                    
                    
        
        #CHICAIA
        if chicaIA == "show_stage" and (bonnieIA == "backstage" or bonnieIA == "west_hall"):
            cIA = random.randint(1,200)
            if cIA == 15:
                show_stage.image = "Show Stage(No_chica)"
                dining_area.image= "Dining Area(Chica)"
                chicaIA = "dining_area"
        elif chicaIA == "dining_area":
            cIA = random.randint(1,200)
            if cIA == 43:
                dining_area.image = "Dining_Area"
                restrooms.image = "Restrooms(Chica)"
                chicaIA = "restrooms"
        elif chicaIA == "restrooms":
            cIA = random.randint(1,200)
            if cIA == 73:
                restrooms.image = "Restrooms"
                chicaIA = "kitchen"
        
        elif chicaIA == "kitchen":
            cIA = random.randint(1,200)
            if cIA == 63:
                east_hall.image = "East Hall(Chica)"
                chicaIA = "east hall"
        
        elif chicaIA == "east hall":
            cIA = random.randint(1,200)
            if cIA == 32:
                east_hall.image = "East Hall"
                e_hall_corner.image = "E.Hall Coner(Chica)"
                chicaIA = "e_hall_corner"
        
        elif chicaIA == "e_hall_corner":
            cIA = random.randint(1,200)
            if cIA == 32:
                e_hall_corner.image= "E. Hall Corner"
                oficina3.image = "oficina(Chica)"
                chicaIA = "oficina"
        
        elif chicaIA == "oficina":
            cIA = random.randint(1,200)
            if cIA == 23:
                if dor2 == "on":
                    UbiC = random.randint(1,3)
                    if UbiC == 1:
                        chicaIA = "dining_area"
                        oficina3.image = "oficina(light_right)"
                        if time == 12:
                            time = 1
                        elif time >= 1:
                            time += 1
                    elif UbiC == 2:
                        chicaIA = "restrooms"
                        oficina3.image = "oficina(light_right)"
                        if time == 12:
                            time = 1
                        elif time >= 1:
                            time += 1
                    elif UbiC == 3:
                        chicaIA = "kitchen"
                        oficina3.image = "oficina(light_right)"
                        if time == 12:
                            time = 1
                        elif time >= 1:
                            time += 1
                elif dor2 == "off":
                    
                    if mode2 == "camaras":
                        jumpscareC = "on"
         
                    
def on_mouse_down(button, pos):
    global mode,mode2,num_cam,bonnieIA,dor,light,dor2,light2,chicaIA,jumpscareB,jumpscareC
    #new game
    
    if mode == "menu":
        if N_G.collidepoint(pos):
            mode = "intro"
    elif mode == "intro":
        mode = "noche1"
        mode2 = "oficina"
    
   
    # Puerta izquierda
    if mode == "noche1":
        if Button_D_L.collidepoint(pos):
            dor = "on" if dor == "off" else "off"
            
    # Luz izquierda
    if mode == "noche1":
        if Button_L_L.collidepoint(pos):
            if light == "off": 
                light = "on"
                light2 = "off"
            else:
                light = "off"
            

    # Puerta derecha
    if mode == "noche1":
        if Button_D_R.collidepoint(pos):
            dor2 = "on" if dor2 == "off" else "off"
            

    # Luz derecha
    if mode == "noche1":
        if Button_L_R.collidepoint(pos):
            if light2 == "off": 
                light2 = "on"
                light = "off"
            else:
                light2 = "off"
            
#seleccion de camaras
    
    if mode2 == "camaras":
        if cam1a.collidepoint(pos):
            num_cam = "cam1a"
        elif cam1b.collidepoint(pos):
            num_cam = "cam1b"
        elif cam5.collidepoint(pos):
            num_cam = "cam5"
        elif cam1c.collidepoint(pos):
            num_cam = "cam1c"
        elif cam3.collidepoint(pos):
            num_cam = "cam3"
        elif cam2a.collidepoint(pos):
            num_cam = "cam2a"
        elif cam2b.collidepoint(pos):
            num_cam = "cam2b"
        elif cam7.collidepoint(pos):
            num_cam = "cam7"
        elif cam6.collidepoint(pos):
            num_cam = "cam6"
        elif cam4a.collidepoint(pos):
            num_cam = "cam4a"
        elif cam4b.collidepoint(pos):
            num_cam = "cam4b"
    
    if jumpscareB == "on":
        if jumpscareBonnie.collidepoint(pos):
            
            mode2 = "nada"
            mode = "menu"
    
    if jumpscareC == "on":
        if jumpscareChica.collidepoint(pos):
            mode2 = "nada"
            mode = "menu"
        
def draw():
    global mode,mode2,num_cam,bonnieIA,dor,light,dor2,light2,jumpscareC,jumpscareB,time
    #fondo de menu
    if mode == "menu":
        fondoM.draw()
        titulo.draw()
        C.draw()
        #Static
        Static.draw()
        N_G.draw()
    
    elif mode == "intro":
        screen.fill("black")
        intro.draw()
        
    elif mode == "noche1":
        screen.fill("black")
        noche1.draw()
        
    
    if mode2 == "oficina":
        Button_L_L.draw()
        Button_D_L.draw()
        Button_L_R.draw()
        Button_D_R.draw()
        fan.draw()
        barra.draw()
    
    if mode == "noche1":
        oficina.draw()

        
    if light == "on":
       
        oficina2.draw() 

        
    if dor == "on":
            dor_L.draw()  
        
    if light2 == "on":
        oficina3.draw()

        
    if dor2 == "on":
            dor_R.draw()  
    


       
    if mode == "noche1":
        Button_L_L.image = "Button_light_lefT(on)" if light == "on" else "Button_light_lefT"
        Button_L_L.draw()
        Button_D_L.image = "Button_door_left(on)" if dor == "on" else "Button_door_left"
        Button_D_L.draw()
        fan.draw()
        barra.draw()
        Button_L_R.image = "Button_light_Right(on)" if light2 == "on" else "Button_light_Right"
        Button_L_R.draw()
        Button_D_R.image = "Button_door_right(on)" if dor2 == "on" else "Button_door_right"
        Button_D_R.draw()
    
    if mode2 == "camaras":
        if num_cam == "cam1a":
            screen.fill("black")
            show_stage.draw()
            Static.draw()
            mapa.draw()
            cam1a.draw()
            cam1b.draw()
            cam5.draw()
            cam1c.draw()
            cam3.draw()
            cam2a.draw()
            cam2b.draw()
            cam7.draw()
            cam6.draw()
            cam4a.draw()
            cam4b.draw()
            barra.draw()
        
        elif num_cam == "cam1b":
            screen.fill("black")
            dining_area.draw()
            Static.draw()
            mapa.draw()
            cam1a.draw()
            cam1b.draw()
            barra.draw()
        elif num_cam == "cam5":
            screen.fill("black")
            backstage.draw()
            Static.draw()
            mapa.draw()
            cam1a.draw()
            cam1b.draw()
            barra.draw()
        elif num_cam == "cam1c":
            screen.fill("black")
            pirates_cove.draw()
            Static.draw()
            mapa.draw()
            cam1a.draw()
            cam1b.draw()
            barra.draw()
        elif num_cam == "cam3":
            screen.fill("black")
            supply_closet.draw()
            Static.draw()
            mapa.draw()
            cam1a.draw()
            cam1b.draw()
            barra.draw()
        elif num_cam == "cam2a":
            screen.fill("black")
            west_hall.draw()
            Static.draw()
            mapa.draw()
            cam1a.draw()
            cam1b.draw()
            barra.draw()
        elif num_cam == "cam2b":
            screen.fill("black")
            w_hall_corner.draw()
            Static.draw()
            mapa.draw()
            cam1a.draw()
            cam1b.draw()
            barra.draw()
        elif num_cam == "cam7":
            screen.fill("black")
            restrooms.draw()
            Static.draw()
            mapa.draw()
            cam1a.draw()
            cam1b.draw()
            barra.draw()
        elif num_cam == "cam6":
            screen.fill("black")
            Static.draw()
            mapa.draw()
            cam1a.draw()
            cam1b.draw()
            barra.draw()
        elif num_cam == "cam4a":
            screen.fill("black")
            east_hall.draw()
            Static.draw()
            mapa.draw()
            cam1a.draw()
            cam1b.draw()
            barra.draw()
        elif num_cam == "cam4b":
            screen.fill("black")
            e_hall_corner.draw()
            Static.draw()
            mapa.draw()
            cam1a.draw()
            cam1b.draw()
            barra.draw()
    
    if mode == "noche1":
        if jumpscareB == "on":
            jumpscareBonnie.draw()
            
            
    if mode == "noche1":
        if jumpscareC == "on":
            jumpscareChica.draw()
            
    
    if mode == "noche1":
        screen.draw.text(str(time) + " AM", (900, 20), fontsize=35, color="white")
    
def on_mouse_move(pos):
    global mode,mode2,bonnieIA,dor

    x, y = pos
    #oficina
    if mode2 == "oficina":
        centro = WIDTH / 2 
        zona_sin_movimiento = 50 
        limite_izquierdo = centro - zona_sin_movimiento
        limite_derecho = centro + zona_sin_movimiento
        
        if x < limite_izquierdo and oficina.x < 790:  
            oficina.x += 20
            oficina2.x += 20
            oficina3.x += 20
            
            fan.x += 20
            dor_L.x += 20
            Button_D_L.x += 20
            Button_L_L.x += 20
            Button_L_R.x += 20
            Button_D_R.x += 20
            dor_R.x += 20
            
            
        elif x > limite_derecho and oficina.x > 260:
            oficina.x -= 20
            oficina2.x -= 20
            oficina3.x -= 20
            
            fan.x -= 20  
            dor_R.x -= 20
            
            dor_L.x -= 20
            Button_D_L.x -= 20
            Button_L_L.x -= 20
            Button_L_R.x -= 20
            Button_D_R.x -= 20
        if y >= 563:
            mode2 = "camaras"
            
               
    elif mode2 == "camaras":
        if y >= 563:
            mode2 = "oficina"
