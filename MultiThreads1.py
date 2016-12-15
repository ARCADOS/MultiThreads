import os, sys, thread, time
import subprocess

def time():
    timeN = time.strftime("%H:%M:%S").split(':')
    return timeN

def main():
    #print '##########################: ',thread.start_new_thread(imprimir_mensaje, (mensaje,))
        #print '#######################################################################'
        #print '           CUANTOS PROCESOS(PROGRAMAS) CORRERAS SIMULTANEAMENTE?       '
        #print '#######################################################################'
        #choise1 = int(raw_input('INGRESE UN ENTERO: '))
        
    thread.start_new_thread(procesos, (treadNow,)
    thread.start_new_thread(opt, (treadNow1,))

    
    
main()
