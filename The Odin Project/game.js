
console.log("Game Started!")

function computerPlay(){
    list = ["Rock", "Paper", "Scissors"]
    // ~~ Aproxima al entero
    return list[~~(Math.random() * list.length)]    
}
function playRound(playerSelection, computerSelection){
    computerSelection = computerSelection.toLowerCase()
    // 0 for the player, 1 for the computer
    winner = 0
    if (playerSelection === computerSelection){
        winner = 2
    }
    switch(playerSelection){
        case "rock":
            switch(computerSelection){
                case "paper":
                    winner = 1
                    break
                case "scissors":
                    break
            }
            break
        case "paper":
            switch(computerSelection){
                case "rock":
                    break;
                case "scissors":
                    winner = 1
                    break
            }
            break
        case "scissors":
            switch(computerSelection){
                case "rock":
                    winner = 1
                    break
                case "paper":
                    break
            }
            break
    }
    switch(winner){
        case 0:
            return "Player Won with " + playerSelection + " vs " + computerSelection +"!!"
        case 1:
            return "Computer Won with " + computerSelection + " vs " + playerSelection +"!!"
        case 2:
            return "Tie with " + playerSelection +"!!"
    }
}

function askPlayer(){
    playerSelection = ""
    while(playerSelection !== "rock" && playerSelection !== "paper" && playerSelection !== "scissors"){
        playerSelection = prompt("Rock, Paper or Scissors??")
        console.log("Player chose " + playerSelection)
        playerSelection = playerSelection.toLowerCase()    
    }
    return playerSelection
}

function game(){
    rounds = 5

    for(let i = 0; i < 5; i++){
        const computerSelection = computerPlay()
        const playerSelection = askPlayer()
        console.log(playRound(playerSelection, computerSelection))
    }
}
window.onload = game()