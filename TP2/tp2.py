import json
import random

choice = input('Ajouter une personne ou tirer ? (ADD, TIRE :) ')
while choice != 'ADD' and choice != 'TIRE':
    choice = input('Ajouter une personne ou tirer ? (ADD, TIRE) : ')

if choice == 'ADD':
    name = input('Entrez votre nom : ')
    end = False
    tickets = []
    while not end or len(tickets) == 0:
        ticket = input('Le num de votre ticket : ')
        tickets.append(ticket)
        skip = input("Continuer ? (OUI / NON)")
        if skip == 'NON':
            end = True

    f = open('tickets.txt', 'a')
    json.dump({"nom": name, "tickets": tickets}, f )
    f.write('\n')
    f.close()
    print('Ticket ajouté au nom de ', name, '!')

if choice == 'TIRE':
    f = open('tickets.txt', 'r')
    doc = f.readlines()
    f.close()

    ticketsTab = []

    for i in range(len(doc)):
        line = eval(doc[i].replace('\n', ''))
        for y in range(len(line['tickets'])):
            ticketsTab.append(line['tickets'][y])

    randomTicket = random.choice(ticketsTab)

    for i in range(len(doc)):
        line = eval(doc[i].replace('\n', ''))
        name = line['nom']
        for y in range(len(line['tickets'])):
            ticket = line['tickets'][y]
            if ticket == randomTicket:
                print(name, 'remporte la tombola avec le ticket', ticket, '!!')