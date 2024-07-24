#! /bin/bash

function ask_to_play() {
    echo Would you like to play a virtual version of 'Rock, Paper, Scissors'?
    read varresponse
    if [ $varresponse == "no" ]
    then
        echo "That's too bad, maybe next time."
    elif [ $varresponse == "yes" ]
    then
        python3 Rock_Paper_Scissors.py
    else
        echo "Please enter 'yes' or 'no'."
        ask_to_play
    fi
}

ask_to_play