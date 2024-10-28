// Game Scenes
const scenes = {
  start: {
    text: "Zilang's day begins with a call to rescue some lost animals. Where should he start?",
    options: [
      { text: "Check the forest", nextScene: "forest" },
      { text: "Look near the river", nextScene: "river" }
    ]
  },
  forest: {
    text: "In the forest, Zilang hears rustling. He spots a baby fox stuck in a bush!",
    options: [
      { text: "Rescue the fox", nextScene: "rescueFox" },
      { text: "Move deeper into the forest", nextScene: "deepForest" }
    ]
  },
  river: {
    text: "By the river, Zilang sees paw prints. It might be a puppy who wandered off.",
    options: [
      { text: "Follow the paw prints", nextScene: "findPuppy" },
      { text: "Call for Niko's help", nextScene: "callNiko" }
    ]
  },
  rescueFox: {
    text: "Zilang frees the fox, who happily joins him. One animal rescued!",
    options: [
      { text: "Go back to start", nextScene: "start" }
    ]
  },
  deepForest: {
    text: "Deeper in the forest, Zilang finds nothing but trees. Time to try somewhere else.",
    options: [
      { text: "Return to start", nextScene: "start" }
    ]
  },
  findPuppy: {
    text: "Following the prints, Zilang finds a lost puppy by the riverbank!",
    options: [
      { text: "Take puppy to van", nextScene: "van" }
    ]
  },
  callNiko: {
    text: "Niko arrives with snacks! Together, they search for animals.",
    options: [
      { text: "Check nearby trees", nextScene: "treeSearch" },
      { text: "Head back to van", nextScene: "van" }
    ]
  },
  treeSearch: {
    text: "In the trees, they find a squirrel needing help. Another rescue complete!",
    options: [
      { text: "Return to start", nextScene: "start" }
    ]
  },
  van: {
    text: "Zilang and Niko have the animals safe in their van. Mission accomplished!",
    options: [
      { text: "Play again", nextScene: "start" }
    ]
  }
};

// Display Scene Function
function displayScene(sceneKey) {
  const scene = scenes[sceneKey];
  document.getElementById('scene').innerText = scene.text;
  document.querySelectorAll('.button').forEach(button => button.remove()); // Clear existing buttons
  
  // Create buttons based on available options
  scene.options.forEach(option => {
    const button = document.createElement('button');
    button.innerText = option.text;
    button.className = 'button';
    button.onclick = () => chooseOption(option.nextScene);
    document.body.appendChild(button);
  });
}

// Start Game
function chooseOption(sceneKey) {
  displayScene(sceneKey);
}

// Initialize the game with the starting scene
displayScene('start');
