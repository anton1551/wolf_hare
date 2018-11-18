"""

Path hare's tracking by wolf simulation with numerical method.

author: Bykov Anton (@anton1551)

"""

import math
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.animation as animation


x_w_start = 0 # starting abscissa of wolf
y_w_start = 100 # starting ordinate of wolf
x_h_start = 0 # starting abscissa of hare
y_h_start = 0 # starting ordinate of hare
velocity_w_start = 12 # velocity of wolf [m/c]
velocity_h_start = 10 # velocity of hare [m/c]
delta_t_start = 0.1 # 

show_animation = True


class State:

    def __init__(self, x_w = 0.0, y_w = 100.0, x_h = 0.0, y_h = 0.0, x_w_old = 0.0, y_w_old = 100.0, x_h_old = -200.0, y_h_old = 0.0, velocity_w = 18, velocity_h = 12, delta_t = 0.1):
        self.x_w = x_w
        self.y_w = y_w
        self.x_h = x_h
        self.y_h = y_h
        self.x_w_old = x_w_old
        self.y_w_old = y_w_old
        self.x_h_old = x_h_old
        self.y_h_old = y_h_old
        self.velocity_w = velocity_w
        self.velocity_h = velocity_h
        self.delta_t = 0.1
        


def update(state):
    state.x_w_old = state.x_w
    state.y_w_old = state.y_w
    state.y_h_old = state.y_h
    state.x_h_old = state.x_h
    
    a_x = state.x_h-state.x_w
    a_y = state.y_h-state.y_w
    
    state.x_w = state.x_w + a_x/math.sqrt(a_x**2+a_y**2)*state.velocity_w*state.delta_t 
    state.y_w = state.y_w + a_y/math.sqrt(a_x**2+a_y**2)*state.velocity_w*state.delta_t 
    state.x_h = state.x_h+state.velocity_h*state.delta_t
    state.y_h = state.y_h

    return state



def main():
    state = State(x_w_start, y_w_start, x_h_start, y_h_start, x_w_old = x_w_start, y_w_old = y_w_start, x_h_old = x_h_start, y_h_old = y_h_start, velocity_w = velocity_w_start, velocity_h = velocity_h_start , delta_t = delta_t_start)

    
    time = 0.0
    x_w = [state.x_w]
    y_w = [state.y_w]
    x_h = [state.x_h]
    y_h = [state.y_h]
    dt = state.delta_t

    while ((state.x_w-state.x_h)**2+(state.y_w-state.y_h)**2)**0.5 >= state.velocity_w*state.delta_t:
        state = update(state)
        
		
        time = time + dt

        x_w.append(state.x_w)
        y_w.append(state.y_w)
        x_h.append(state.x_h)
        y_h.append(state.y_h)       
        

        if show_animation:
            a_x = state.x_h-state.x_w
            a_y = state.y_h-state.y_w
    
            u =  a_x/math.sqrt(a_x**2+a_y**2)*state.velocity_w*state.delta_t 
            v =  a_y/math.sqrt(a_x**2+a_y**2)*state.velocity_w*state.delta_t             
            plt.cla()
            plt.plot(x_w, y_w, ".r", label = "Wolf")
            plt.plot(x_h, y_h, ".g", label = "Hare")                        
            plt.axis("equal")
            plt.grid(True)
            plt.title("Time, s:" + str(time)[:4])            
            plt.pause(0.01)
            circle1 = plt.Circle((0,0),.2,color = 'r')
            plt.gcf().gca().add_artist(circle1)
    
    if show_animation:        
        plt.axis("equal")
        plt.grid(True)        
        plt.grid(True)     
        circle1 = plt.Circle((0,0),.2,color = 'r')
        plt.gcf().gca().add_artist(circle1)
        plt.show()
        


if __name__  == '__main__':
    print("Pure pursuit path tracking simulation WOLF-HARE start")
    main()
