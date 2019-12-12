#!/usr/bin/env python
# -*- coding: utf-8 -*-
import boto3, json, random
sns = boto3.client('sns', region_name='us-east-1')

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

    assignment = {'k': killer, 't': target}

    message = "Hello {a[k]}, your assignment is {a[t]}.".format(a=assignment)

    targets.remove(target)

    print('Sending assignment to',players[killer],'...',end=' ')
    sns.publish(PhoneNumber = players[killer], Message=message)
    print('SENT')
