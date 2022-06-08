# routes

## user

### create user

(username, password) -> user=
creates a user account for a new user

### login

(username,password) -> user
logs the user in to the game

### logout

(this may require user)
() -> none
logs out the current user

## high-scores

### check_highscore

(user, current_score) -> ?

grabs the current highscore if there is one and compares it to the current_score. if current_score is higher then the highscore or there is no highscore creates a new highscore object.

### get_highscore

() -> highscore

returns the current high_Score
