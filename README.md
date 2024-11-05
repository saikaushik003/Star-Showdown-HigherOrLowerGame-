# StarShowdown: A Fun and Interactive Game

Welcome to **StarShowdown**, a thrilling web-based game that challenges players to guess which celebrity has the most Instagram followers. This project combines engaging gameplay, vibrant visuals, and a user-friendly interface, providing a fun experience for players of all ages.
## Game Link
[StarShowdown](https://saikaushik003.github.io/Star-Showdown-HigherOrLowerGame-/)
## Features

### Interactive Gameplay
- Players are presented with two actors, and they must decide which one has more Instagram followers by selecting either "Higher" or "Lower."
- The game dynamically displays images and follower counts for each actor, enhancing user engagement.
- Each correct guess increases the player's score, while an incorrect choice ends the game.

### Score Tracking
- The game features real-time score tracking, displaying both the current score and the highest score achieved in the session.
- Players receive feedback based on their performance, encouraging them to improve with each round.

### Responsive Design
- Built with Tailwind CSS, the game adapts seamlessly to different screen sizes, ensuring an optimal experience on both desktop and mobile devices.
- The layout is clean and user-friendly, making navigation intuitive.

### Fun Visuals and Effects
- The background features vibrant animations that enhance the gaming atmosphere.
- The UI incorporates visually appealing buttons and icons from Bootstrap Icons, improving interaction and aesthetics.
- Custom fonts and color schemes contribute to the overall design, making the game visually striking.

### Unique Feedback System
- Upon game completion, players receive personalized feedback based on their score, complete with playful messages and background images that reflect their performance.
- The feedback system adds a layer of humor and encourages players to share their scores with friends.

## Technology Stack
- **HTML**: The structure of the game is built using semantic HTML5.
- **CSS**: Styling is managed through Tailwind CSS for responsive design and Bootstrap Icons for UI elements.
- **JavaScript**: The game logic, score tracking, and interactive elements are implemented using JavaScript.

## Game Flow
1. **Start Screen**: Players are welcomed with a visually appealing start screen, featuring the game's title and a "Play" button.
2. **Game Screen**: Once the game begins, players are shown two actors with their follower counts. They must choose which actor has more followers.
3. **Score Feedback Screen**: At the end of the game, players receive their scores along with personalized feedback, motivating them to play again.

## Python Console Version: Basic Idea

In addition to the web-based game, **StarShowdown** includes a console-based implementation written in Python, named `basic_idea.py`. This version allows users to play a similar game in a terminal environment. Here's a brief overview of its functionality:

- **Data Handling**: The script reads a CSV file (`insta.csv`) containing actor names, follower counts, and image links. It converts follower counts from strings to numerical values for comparison.
- **Gameplay Mechanics**: Players are presented with two randomly selected actors. They must guess whether the second actor has a higher or lower follower count than the first. The game continues until the player makes an incorrect guess.
- **Visual Representation**: The script displays images of the actors using the PIL library, enhancing the user experience even in a console setting.
- **Scoring System**: Players accumulate points for correct guesses, with their final score displayed at the end of the game.

## Conclusion
**StarShowdown** is not just a game; it's an engaging social experience that taps into pop culture. The combination of fun gameplay, appealing visuals, and dynamic interaction makes it a standout project. Join the fun and see how well you know your celebrities' follower counts!

Feel free to explore the code, contribute to this project, or try out the Python console version. Your feedback and suggestions are always welcome!
