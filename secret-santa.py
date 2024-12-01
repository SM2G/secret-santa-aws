#!/usr/bin/env python
# -*- coding: utf-8 -*-
import boto3, json, random
sns = boto3.client('sns', region_name='eu-west-3')

# Get player data
with open('players.json') as json_file:
    players = json.load(json_file)
    killers = []
    for p in players:
        killers.append(p)
        print('Player',p,'(',players[p],') added.')

targets = killers.copy()
random.shuffle(killers)
random.shuffle(targets)

for killer in killers:
    target=random.choice(targets)
    while killer == target:
        target=random.choice(targets)

    # Assigning targets to players
    assignment = {'k': killer, 't': target}
    message = "Hello {a[k]}, your assignment is {a[t]}.".format(a=assignment)
    targets.remove(target)

    # Sending assignments
    print('Sending assignment to',players[killer],'...',end=' ')
    #print(message)
    sns.publish(PhoneNumber = players[killer], Message=message)
    print('SENT')
