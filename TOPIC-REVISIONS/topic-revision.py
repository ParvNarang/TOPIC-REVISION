''' Developed By - Parv Narang '''

import speech_recognition as sr
import playsound
import time
import random

r = sr.Recognizer()

with sr.Microphone() as source:

    while True:
        playsound.playsound('listen.mp3', True)
        print("What do you want to listen to : ")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('you said: {}'.format(text))
            #text = input()

            if text == 'electricity':
                print("Okay")
                print("In the chapter electricity you will learn about")
                print("electric current, electric circuit, voltage, current, resistance, ohms law, series and parallel, the heating effect, electric power, their applications and much more")
                playsound.playsound('introel.mp3', True)
                
                while True:
                    try:
                        playsound.playsound('topic.mp3', True)
                        print("In electricity which topic you want to listen to ?")
                        #time.sleep(5)
                        audio1 = r.listen(source)
                        text1 = r.recognize_google(audio1)
                        print('{}'.format(text1))
                        #time.sleep(1)
                        if text1 == 'electric current' or text1 == 'current':
                            print(" The flow of electric charge is known as Electric Current. It is expressed in terms of rate of flow of charges. ")
                            print(" The formula for calculating electric current is net charge divided by time to carry the charge. ")
                            print(" The SI unit of current is ampere (A). ")
                            print(" Direction of electric current is same as direction of positive charges and opposite to the direction of flow of negative charges. ")
                            print(" I = Q / t ")
                            playsound.playsound('current.mp3',True)

                        elif text1 == 'potential difference' or text1 == 'voltage':
                            print(" Work done per unit charge in taking charge from one point to another is known as Potential Difference. ")
                            print(" The unit of potential difference is volt (V) ")
                            print(" 1V is defined as the potential difference between two points if 1 Joule of work is done to move 1 coulomb charge from one point to another. ")
                            print(" V = W / Q ")
                            playsound.playsound('pd.mp3',True)

                        elif text1 == 'ohms law' or text1 == '':
                            print(" According to ohms law the potential difference V across 2 ends of a given metallic wire is directly proportional to the current flowing provided its temperature remains the same. ")
                            print(" V ∝ I ")
                            print(" V = IR ")
                            print(" R is a constant known as Resistance. The SI unit of resistance is ohm (Ω) ")
                            playsound.playsound('ohms.mp3',True)


                        elif text1 == 'what are the factors on which the resistance of a conductor depends' or text1 == 'factors on which the resistance of a conductor depends':
                            print(" It is ")
                            print(" directly proportional to the length of conductor. ")
                            print(" inversely proportional to the area of cross section. ")
                            print(" depends on the nature of material. ")
                            print(" directly proportional to the temperature. ")
                            playsound.playsound('factors.mp3',True)
                            

                        elif text1 == 'resistivity':
                            print(" Resistivity is the property of the material. The SI unit of resistivity is ohm-metre. ")
                            print(" It is also called specific resistance. ")
                            print(" Resistance = Resistivity * Length of Conductor/Cross Sectional Area ")
                            print(" Resistivity of metals varies from 10 raised to power minus 8 to 10 raised to power minus 6. ")
                            print(" Resistivity of insulators varies from 10 raised to power 12 to 10 raised to power 17 ")
                            print(" Copper and aluminium are used in electrical transmission due to their low resistivity. ")
                            playsound.playsound('resistivity.mp3',True)

                        elif text1 == 'series circuit' or text1 == 'series' or text1 == 'resistors in series':
                            print(" When two or more resistors are joined in series, then their total resistance is given by the formula- ")
                            print(" R = R1 + R2 + R3 ")
                            print(" The current remains the same. Total voltage is given by - ")
                            print(" V = V1 + V2 + V3 ")
                            playsound.playsound('series.mp3', True)
                        

                        elif text1 == 'parallel circuit' or text1 == 'parallel' or text1 == 'resistors in parallel':
                            print(" When two or more resistors are joined in parallel, then their total resistance is given by the formula- ")
                            print(" 1/R = 1/R1 + 1/R2 + 1/R3 ")
                            print(" The voltage remains the same across each resistor. Total current is given by - ")
                            print(" I = I1 + I2 + I3 ")
                            playsound.playsound('parallel.mp3', True)

                        elif text1 == 'advantages of parallel combination over series combination':
                            print(" If one component fails in series combination, then complete circuit is broken and no component can work properly. ")
                            print(" Different appliances need different current to operate, this can be met through parallel. ")
                            playsound.playsound('adv.mp3', True)

                        elif text1 == 'heating effect of electric current' or text1 == 'heating effect' or text1 == 'the heating effect':
                            print(" When charge Q moves against the potential difference V in time t, the amount of work is given by - ")
                            print(" W = V x Q ")
                            print(" W = V x Q/t x t ")
                            print(" W = V x I x t ")
                            playsound.playsound('heating.mp3', True)

                        elif text1 == 'joules law of heating' or text1 == 'joules law':
                            print(" Heat produced in a resistor is directly proportional to square root of current. ")
                            print(" It is also directly proportional to resistance for a given current. ")
                            print(" Also, directly proportional to time. ")
                            print(" H = I square x R x t ")
                            playsound.playsound('joule.mp3', True)

                        elif text1 == 'what is a fuse' or text1 == 'fuse':
                            print(" Electric fuse is a safety device to protect the electrical appliance from short circuit. ")
                            print(" It is connected in series with the circuit. ")
                            print(" It melts when more than the required current flows through the circuit. ")
                            playsound.playsound('fuse.mp3', True)

                        elif text1 == 'filament of bulb' or text1 == 'what is the filament of the bulb made up of':
                            print(" Filament of electric bulb is made up of tungsten because it has a very high melting point. ")
                            print(" And also does not oxidize readily at high temperatures. ")
                            playsound.playsound('filament.mp3', True)

                        elif text1 == 'power' or text1 == 'electric power':
                            print(" The rate at which electric energy is dissipated or consumed in an electric current. ")
                            print(" The SI unit of power is Watt. ")
                            print(" The commercial unit of electric energy is kilowatt hour KWh. ")
                            print(" P = VI ")
                            print(" P = I square x R ")
                            print(" P = V square / R")
                            playsound.playsound('power.mp3', True)
                            

                        elif text1 == 'no questions' or text1 == 'nothing' or text1 == 'no':
                            print("Okay")
                            playsound.playsound('ok.mp3',True)
                            break

                        else:
                            print("Sorry please say it again")
                            playsound.playsound('sorry_please.mp3',True)
                    except:
                        print("Sorry ask again")
                        playsound.playsound('sorry_ask.mp3',True)

            elif text == 'our environment' or text == 'environment' or text == 'enviroment':
                print(" Okay ")
                print(" In the chapter our environment we are going to study about - ")
                print(" its components, ecosystem, food chain, food web, biological magnification, ozone layer , ozone depletion, waste disposal and its types " )
                playsound.playsound('introenv.mp3', True)
                
                while True:
                    try:
                        
                        playsound.playsound('topic1.mp3', True)
                        print("In the chapter our environment what topic do you want to listen")
                        #time.sleep(5)
                        audio2 = r.listen(source)
                        text2 = r.recognize_google(audio2)
                        print('{}'.format(text2))
                        #time.sleep(1)
                        if text2 == 'enviroment' or text2 == 'what is environment' or text2 == 'environment':
                            print(" Things around us is known as an Environment. ")
                            print(" It consists of living component also known as biotic component and non-living component also known as Abiotic Component." )
                            playsound.playsound('env.mp3', True)
                           

                        elif text2 == 'ecosystem' or text2 == 'what is an ecosystem':
                            print(" The interaction between abiotic and biotic components is defined as ecosystem. ")
                            print(" It is a self sustaining and functional unit of biosphere. ")
                            playsound.playsound('eco.mp3', True)                            

                        
                        elif text2 == 'what are the types of ecosystem' or text2 == 'types of ecosystem':
                            print(" There are two types of ecosystem- natural ecosystem and artificial ecosystem. ")
                            print(" The ecosystem present naturally is known as Natural Ecosystem. Example of Natural Ecosystem are forests, grasslands, deserts, ponds, lakes, rivers, estuaries, sea etc. ")
                            print(" The ecosystem which is man-made is known as Artificial Ecosystem. For Example Gardens, Aquariums and Agro ecosystem which is the largest manmade ecosystem. ")
                            playsound.playsound('tyeco.mp3', True)
                            
                            
                        elif text2 == 'what are the abiotic factors' or text2 == 'what are the factors of abiotic components' or text2 == 'abiotic factors':
                            print(" Abiotic Factors Include - Climatic factors such as rain, temperature, wind etc. Another abiotic factor is edaphic factors such as soil, pH, minerals. ")
                            playsound.playsound('abfact.mp3', True)
                            

                        elif text2 == 'what are the biotic factors' or text2 == 'what are the factors of abiotic components' or text2 == 'biotic factors':
                            print(" Biotic Factors Include- ")
                            print(" Producers - which can make their own food, such as plants, blue green algae etc. ")
                            print(" Consumers - which feed on producers. Such as herbivores. In consumers there are- primary consumers, secondary consumers, tertiary consumers etc.")
                            print(" Carnivores -  are flesh eating animals. ")
                            print(" Omnivores - consume both plants and animals. ")
                            print(" Parasites - which live inside and depend upon living host. ")
                            print(" Saprophytes - which feed on dead remains of plants and animals. ")
                            playsound.playsound('bfact.mp3', True)
                            

                        elif text2 == 'what is a food chain' or text2 == 'food chain':
                            print(" Food Chain is defined as series of organisms in order in which organisms feeds on another organism. ")
                            print(" There are various steps in food chain in which energy is transferred, each level is known as trophic level. Energy is always transferred unidirectionally. ")
                            playsound.playsound('fdch.mp3', True)
                            

                        elif text2 == 'what are the characteristics of food chain' or text2 == 'characteristics of food chain':
                            print(" There is a unidirectional flow of energy from producers to consumers. ")
                            print(" There are generally 3 to 4 trophic levels. ")
                            print(" It is always straight ")
                            print(" Organism can occupy different trophic levels in different food chain.")
                            playsound.playsound('chfc.mp3', True)

                        elif text2 == 'what is the ten percent law' or text2 == 'ten percent law':
                            print(" A 10 percent law is followed in energy transfer ")
                            print(" this law states that only 10 percent of energy is transferred from one trophic level to another trophic level. ")
                            print(" The remaining 90 percent will be used by the present trophic level in different processes. ")
                            print(" Therefore there are usually 3-4 trophic levels in a food chain. ")
                            playsound.playsound('ten.mp3', True)

                        
                        elif text2 == 'what is a food web' or text2 == 'foodweb' or text2 == 'what is a foodweb' or text2 == 'food web':
                            print(" Interconnection of food chain is known as Food Web. It shows how food chain are interdependent. ")
                            playsound.playsound('fdw.mp3', True)

                        elif text2 == 'characteristics of food web' or text2 == 'what are the characteristics of food web':
                            print(" Food webs are never straight as they are formed by interlinking of food chains. ")
                            print(" Food web provides alternative pathways of food availability. If a particular species is destroyed, the predator can feed on an alternative species. ")
                            print(" Food webs increase ecosystem stability. ")
                            playsound.playsound('chwb.mp3', True)

                        elif text2 == 'Biological magnification' or text2 == 'biomagnification' or text2 == 'what is biological magnification' or text2 == 'what is biomagnification':
                            print(" The concentration of harmful substances increases with every trophic level. This is known as Biomagnification. ")
                            print(" Addition of pesticides in one trophic level increases the concentration of pesticides in other trophic level. ")
                            playsound.playsound('bm.mp3', True)

                        elif text2 == 'what is ozone layer' or text2 == 'ozone layer':
                            print(" High UV radiation break down oxygen into oxygen atoms. These oxygen atoms when combine with oxygen, they form ozone. ")
                            playsound.playsound('ol.mp3', True)

                        elif text2 == 'what is depletion of ozone layer' or text2 == 'depletion of ozone layer':
                            print(" When the thickness of ozone layer decreases it is called ozone depletion ")
                            playsound.playsound('od.mp3', True)

                        elif text2 == 'how is ozone depletion caused' or text2 == 'cause of ozone depletion':
                            print(" This is due to excessive use of chlorofluorocarbons in refrigerators, ACs, aerosols, etc. ")
                            playsound.playsound('odc.mp3', True)

                        elif text2 == 'what could ozone depletion lead to' or text2 == 'ozone depletion leads to ' or text2 == 'consequences' or text2 == 'what are the consequences of ozone depletion':
                            print(" Thinning of ozone would allow penetration of Ultraviolet rays into earth’s atmosphere causing blindness, skin cancers and mutations. ")
                            playsound.playsound('odl.mp3', True)

                        elif text2 == 'which agreement was passed to limit the use of CFC' or text2 == 'what agreement' or text2 == 'which agreement':
                            print(" In 1987 United Nations Environment Programme (UNEP) signed an agreement to limit the usage of CFCS.")
                            playsound.playsound('unep.mp3', True)
                            

                        elif text2 == 'what is garbage' or text2 == 'garbage':
                            print(" Waste materials are known as garbage or simply waste. ")
                            playsound.playsound('waste.mp3', True)

                        elif text2 == 'what are the two types of garbage' or text2 == 'two types of garbage' or text2 == 'what are the two types of waste' or text2 == 'two types of waste':
                            print(" There are two types of garbage - Biodegradable Waste and Non-biodegradable Waste. ")
                            playsound.playsound('bdnbd.mp3', True)

                        elif text2 == 'what is biodegradable waste' or text2 == 'biodegradable waste':
                            print(" Garbage that can be completely decomposed by the microorganism are called Biodegradable Garbage. Such as fruit and vegetable peel, sewage. ")
                            playsound.playsound('bd.mp3', True)

                        elif text2 == 'what is non biodegradable waste' or text2 == 'non biodegradable waste' or text2 == 'nonbiodegradable waste' or text2 == 'what is nonbiodegradable waste':
                            print(" Substances which cannot be decomposed through microorganisms are known as Non-biodegradable Garbage, For Example, Plastic, Glass, Pesticide, Metals, Radioactive Elements etc. ")
                            playsound.playsound('nbd.mp3', True)


                        elif text2 == 'what are the methods of waste management' or text2 == 'methods of waste management' or text2 == 'waste management':
                            print(" Waste disposal is a very important part of day to day life. ")
                            print(" There are different methods of waste disposal management- sewage treatment plant, biogas plant, land fillings, recycling, incineration, composting and reuse. ")
                            playsound.playsound('wstd.mp3', True)
                      
                        elif text2 == 'no questions' or text2 == 'nothing' or text2 == 'no':
                            print("Okay")
                            playsound.playsound('ok.mp3',True)
                            break

                        else:
                            print("Sorry please say it again")
                            playsound.playsound('sorry_please.mp3',True)
                    
                    except:
                        print("Sorry ask again")
                        playsound.playsound('sorry_ask.mp3',True)
            
            elif text == 'some questions' or text == 'quiz' or text == 'questions' or text == 'question':
                print(" Okay ")
                print(" So I will ask some questions ")
                print(" You will have to answer each question in a span of 10 seconds each ")

                while True:
                    try:
                        
                        sent = ["what is the unit of potential difference?", "what is the SI unit of resistance?", "what is food web?", "what is an ecosystem?","what is an environment?", "what is resistivity also called?"]
                        num = random.randrange(0,6)
                        print(sent[num])
                        if sent[num] == 'what is the unit of potential difference?':
                            time.sleep(5)
                            print("d")
                            time.sleep(2)
                            audio3 = r.listen(source)
                            text3 = r.recognize_google(audio3)
                            print('{}'.format(text3))
                            #text3 = input()
                            if text3 == 'volt' or text3 == 'V':
                                print("Correct")
                                continue
                            elif text3 == 'exit':
                                break
                            else:
                                print("Incorrect")

                        elif sent[num] == 'what is the SI unit of resistance?':
                            time.sleep(5)
                            print("s")
                            time.sleep(2)
                            audio3 = r.listen(source)
                            text3 = r.recognize_google(audio3)
                            print('{}'.format(text3))
                            #text3 = input()
                            if text3 == 'ohm':
                                print("Correct")
                                continue
                            elif text3 == 'exit':
                                break
                            else:
                                print("Incorrect")
                           
                        elif sent[num] == 'what is food web?':
                            time.sleep(5)
                            print("w")
                            time.sleep(2)
                            audio3 = r.listen(source)
                            text3 = r.recognize_google(audio3)
                            print('{}'.format(text3))
                            #text3 = input()
                            if text3 == 'interconnection of food chains' or text3 == 'interconnection of food chain':
                                print("Correct")
                                continue
                            elif text3 == 'exit':
                                break
                            else:
                                print("Incorrect")

                        elif sent[num] == 'what is an ecosystem?':
                            time.sleep(5)
                            print("w")
                            time.sleep(2)
                            audio3 = r.listen(source)
                            text3 = r.recognize_google(audio3)
                            print('{}'.format(text3))
                            #text3 = input()
                            if text3 == 'interaction of biotic and abiotic components' or text3 == 'the interaction between biotic components and abiotic components':
                                print("Correct")
                                continue
                            elif text3 == 'exit':
                                break
                            else:
                                print("Incorrect")

                        elif sent[num] == 'what is an environment?':
                            time.sleep(5)
                            print("w")
                            time.sleep(2)
                            audio3 = r.listen(source)
                            text3 = r.recognize_google(audio3)
                            print('{}'.format(text3))
                            #text3 = input()
                            if text3 == 'things around us is known as an environment' or text3 == 'things around us':
                                print("Correct")
                                continue
                            elif text3 == 'exit':
                                break
                            else:
                                print("Incorrect")

                        elif sent[num] == 'what is resistivity also called?':
                            time.sleep(5)
                            print("w")
                            time.sleep(2)
                            audio3 = r.listen(source)
                            text3 = r.recognize_google(audio3)
                            print('{}'.format(text3))
                            #text3 = input()
                            if text3 == 'specific resistance':
                                print("Correct")
                                continue
                            elif text3 == 'exit':
                                break
                                
                            else:
                                print("Incorrect")

                        else:
                            print("nothing")
                     
                    except:
                        print("asd")
     
            else:
                print("Sorry not in the list")
                playsound.playsound('sorry_list.mp3',True)
        
        except:
            print("Sorry could not recognize")
            playsound.playsound('sorry_recog.mp3',True)
