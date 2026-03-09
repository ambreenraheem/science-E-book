import { useState } from "react";

const TOPICS = [
  { id:"body",     title:"Our Body",        color:"#C0392B", bg:"#FDF0EE", img:"https://images.unsplash.com/photo-1530026186672-2cd00ffc50fe?w=420&h=230&fit=crop",
    icon:<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" width="26" height="26"><circle cx="20" cy="8" r="4"/><path d="M13 16h14M20 16v12M13 28l-3 7M27 28l3 7M13 21l-3 4M27 21l3 4"/></svg> },
  { id:"senses",   title:"Five Senses",     color:"#6C3483", bg:"#F5EEF8", img:"https://images.unsplash.com/photo-1516585427167-9f4af9627e6c?w=420&h=230&fit=crop",
    icon:<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" width="26" height="26"><ellipse cx="20" cy="20" rx="15" ry="9"/><circle cx="20" cy="20" r="5"/><circle cx="20" cy="20" r="2" fill="currentColor"/></svg> },
  { id:"animals",  title:"Animals",         color:"#1E8449", bg:"#EAFAF1", img:"https://images.unsplash.com/photo-1474511320723-9a56873867b5?w=420&h=230&fit=crop",
    icon:<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" width="26" height="26"><ellipse cx="20" cy="24" rx="11" ry="8"/><circle cx="10" cy="13" r="4"/><circle cx="30" cy="13" r="4"/><circle cx="16" cy="22" r="1.5" fill="currentColor"/><circle cx="24" cy="22" r="1.5" fill="currentColor"/><path d="M18 27 Q20 30 22 27"/></svg> },
  { id:"plants",   title:"Plants",          color:"#27AE60", bg:"#EDFAF1", img:"https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=420&h=230&fit=crop",
    icon:<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" width="26" height="26"><path d="M20 36V18"/><path d="M20 26 Q11 18 11 8 Q20 8 20 18"/><path d="M20 21 Q29 15 31 5 Q22 5 20 15"/><path d="M15 34 Q20 32 25 34"/></svg> },
  { id:"magnet",   title:"Magnets",         color:"#1A5276", bg:"#EBF5FB", img:"https://images.unsplash.com/photo-1518770660439-4636190af475?w=420&h=230&fit=crop",
    icon:<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" width="26" height="26"><path d="M10 8 L10 22 Q10 32 20 32 Q30 32 30 22 L30 8"/><path d="M8 8 L16 8M24 8 L32 8"/><line x1="3" y1="16" x2="9" y2="16"/><line x1="31" y1="16" x2="37" y2="16"/></svg> },
  { id:"space",    title:"Space",           color:"#154360", bg:"#EAF2FF", img:"https://images.unsplash.com/photo-1462331940025-496dfbfc7564?w=420&h=230&fit=crop",
    icon:<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" width="26" height="26"><circle cx="20" cy="20" r="7"/><path d="M20 3v4M20 33v4M3 20h4M33 20h4M8 8l3 3M29 29l3 3M32 8l-3 3M11 29l-3 3"/></svg> },
  { id:"machines", title:"Simple Machines", color:"#784212", bg:"#FEF5E7", img:"https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=420&h=230&fit=crop",
    icon:<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" width="26" height="26"><circle cx="20" cy="20" r="9"/><circle cx="20" cy="20" r="3"/><path d="M20 11v-5M20 29v5M11 20H6M29 20h5M13.5 13.5l-3.5-3.5M26.5 26.5l3.5 3.5M26.5 13.5l3.5-3.5M13.5 26.5l-3.5 3.5"/></svg> },
  { id:"weather",  title:"Water & Weather", color:"#0E6655", bg:"#E8F8F5", img:"https://images.unsplash.com/photo-1504608524841-42584120d693?w=420&h=230&fit=crop",
    icon:<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" width="26" height="26"><path d="M6 24 Q6 17 13 17 Q13 10 20 10 Q27 10 27 17 Q34 17 34 24 Q34 31 20 31 Q6 31 6 24Z"/><path d="M15 33L13 38M20 33L20 38M25 33L23 38"/></svg> },
];

const TYPE_CFG = {
  mcq:      { label:"Multiple Choice", bg:"#EFF6FF", color:"#1D4ED8", border:"#BFDBFE" },
  scramble: { label:"Spell It Right!",  bg:"#FFF7ED", color:"#C2410C", border:"#FED7AA" },
  image:    { label:"Spot It!",         bg:"#F0FDF4", color:"#15803D", border:"#BBF7D0" },
  history:  { label:"History Fact",     bg:"#FDF4FF", color:"#7E22CE", border:"#E9D5FF" },
};

const QUESTIONS = {
  body: [
    { type:"mcq",     q:"Which organ pumps blood around your body?", choices:["Brain","Heart","Lungs","Stomach"], ans:1, img:"https://images.unsplash.com/photo-1628348068343-c6a848d2b6dd?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"How many bones does an adult human body have?", choices:["106","206","306","406"], ans:1, img:"https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"What is the main job of our lungs?", choices:["Digest food","Pump blood","Help us breathe","Move our arms"], ans:2 },
    { type:"mcq",     q:"How many chambers does the human heart have?", choices:["Two","Three","Four","Five"], ans:2 },
    { type:"mcq",     q:"What carries oxygen through the blood?", choices:["White blood cells","Red blood cells","Platelets","Plasma"], ans:1 },
    { type:"mcq",     q:"Which organ cleans the blood and removes waste from the body?", choices:["Stomach","Liver","Kidneys","Heart"], ans:2 },
    { type:"history", q:"William Harvey discovered in 1628 that the heart pumps blood in a continuous ___ around the body.", choices:["Zigzag","Loop / Circle","Straight line","Spiral"], ans:1, fact:"In 1628, William Harvey published proof that the heart pumps blood in a continuous loop. Before this, people believed blood was made fresh every day! He changed medicine forever." },
    { type:"history", q:"Ancient Egyptians believed that thinking happened in the heart, not the ___.", choices:["Stomach","Lungs","Brain","Liver"], ans:2, fact:"Ancient Egyptians thought the heart was the seat of thought and feeling. When making mummies, they threw the brain away but kept the heart! It wasn't until ancient Greece that the brain's role was understood." },
    { type:"image",   q:"What part of the body is shown in this X-ray picture?", choices:["Skull","Spine","Full Skeleton","Ribcage"], ans:2, img:"https://images.unsplash.com/photo-1559757148-5c350d0d3c56?w=440&h=270&fit=crop" },
    { type:"image",   q:"Which important organ does this model show?", choices:["Stomach","Kidney","Heart","Liver"], ans:2, img:"https://images.unsplash.com/photo-1628348068343-c6a848d2b6dd?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this body part!", scrambled:"RATHE", choices:["HEART","LUNGS","BRAIN","LIVER"], ans:0 },
    { type:"scramble", q:"Unscramble this body part!", scrambled:"GULNS", choices:["BONES","LUNGS","SPINE","HEART"], ans:1 },
    { type:"scramble", q:"Unscramble this body part!", scrambled:"NIABR", choices:["BRAIN","HEART","SPINE","NERVE"], ans:0 },
  ],

  senses: [
    { type:"mcq",     q:"Which sense do we use when we smell a flower?", choices:["Sight","Hearing","Smell","Touch"], ans:2, img:"https://images.unsplash.com/photo-1490750967868-88df5691cc27?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"Which body part helps us see the world?", choices:["Nose","Ears","Eyes","Tongue"], ans:2 },
    { type:"mcq",     q:"What sense do we use when we listen to music?", choices:["Taste","Hearing","Smell","Sight"], ans:1, img:"https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"Which sense tells us if food is sweet, salty or sour?", choices:["Touch","Smell","Sight","Taste"], ans:3 },
    { type:"mcq",     q:"What body part do we use to feel if something is hot, cold or rough?", choices:["Eyes","Ears","Skin","Nose"], ans:2 },
    { type:"mcq",     q:"How many main senses does the human body have?", choices:["3","4","5","6"], ans:2 },
    { type:"history", q:"The ancient Greek thinker Aristotle was the first to name and describe the five senses. He lived roughly ___ years ago.", choices:["About 100","About 500","About 2,300","About 5,000"], ans:2, fact:"Aristotle (384–322 BC) was the first thinker to formally describe and name the five senses: sight, hearing, smell, taste, and touch. That was over 2,300 years ago!" },
    { type:"history", q:"Louis Braille lost his sight at age 3 and went on to invent a reading system for blind people using raised ___.", choices:["Lines","Dots","Squares","Arrows"], ans:1, fact:"Louis Braille (1809–1852) became blind at age 3. By age 15 he invented the Braille system — a code of raised dots that blind people can read by touch. Today it is used worldwide!" },
    { type:"image",   q:"Which sense organ is shown in this close-up picture?", choices:["Ear","Nose","Eye","Tongue"], ans:2, img:"https://images.unsplash.com/photo-1516585427167-9f4af9627e6c?w=440&h=270&fit=crop" },
    { type:"image",   q:"We use this sense to feel textures like rough or smooth. What sense is being used?", choices:["Smell","Taste","Hearing","Touch"], ans:3, img:"https://images.unsplash.com/photo-1583947215259-38e31be8751f?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this sense word!", scrambled:"LEMLS", choices:["SMELL","TASTE","SIGHT","TOUCH"], ans:0 },
    { type:"scramble", q:"Unscramble this sense word!", scrambled:"HTOUC", choices:["TASTE","SMELL","TOUCH","SIGHT"], ans:2 },
  ],

  animals: [
    { type:"mcq",     q:"Which animal is known as the King of the Jungle?", choices:["Tiger","Lion","Elephant","Giraffe"], ans:1, img:"https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"How do fish breathe underwater?", choices:["Lungs","Skin","Gills","Nose"], ans:2, img:"https://images.unsplash.com/photo-1524704796725-9fc3044a58b2?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"Which animal can change its skin colour to hide from enemies?", choices:["Dog","Chameleon","Horse","Deer"], ans:1 },
    { type:"mcq",     q:"Which animal has the longest neck in the whole world?", choices:["Elephant","Giraffe","Camel","Horse"], ans:1 },
    { type:"mcq",     q:"What do caterpillars turn into after their chrysalis stage?", choices:["Birds","Worms","Butterflies","Spiders"], ans:2, img:"https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"What is the fastest land animal on Earth?", choices:["Lion","Horse","Cheetah","Leopard"], ans:2 },
    { type:"mcq",     q:"What is a group of wolves called?", choices:["Herd","Pack","Flock","Pride"], ans:1 },
    { type:"history", q:"Aristotle wrote the world's first book about animals around 350 BC. He described roughly how many species?", choices:["About 50","About 500","About 50,000","About 5,000"], ans:1, fact:"Around 350 BC, Aristotle wrote 'History of Animals,' describing about 500 species. He is called the Father of Zoology — the science of animals — making him the world's first scientist to classify living things!" },
    { type:"history", q:"Charles Darwin discovered that animals change slowly over many generations to survive. This idea is called ___.", choices:["Gravity","Evolution","Photosynthesis","Migration"], ans:1, fact:"In 1859, Charles Darwin published 'On the Origin of Species,' explaining that all animals (and humans!) evolved slowly over millions of years. It is one of the most important ideas in all of science!" },
    { type:"image",   q:"Which big cat is shown in this photo?", choices:["Tiger","Cheetah","Lion","Leopard"], ans:2, img:"https://images.unsplash.com/photo-1546182990-dffeafbe841d?w=440&h=270&fit=crop" },
    { type:"image",   q:"Name this tall African animal!", choices:["Camel","Horse","Giraffe","Zebra"], ans:2, img:"https://images.unsplash.com/photo-1547721064-da6cfb341d50?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this animal name!", scrambled:"LAEGE", choices:["EAGLE","SNAKE","WHALE","TIGER"], ans:0 },
    { type:"scramble", q:"Unscramble this animal name!", scrambled:"LHAEW", choices:["SHARK","EAGLE","HORSE","WHALE"], ans:3 },
  ],

  plants: [
    { type:"mcq",     q:"What do plants use sunlight to make?", choices:["Water","Food (Sugar)","Air","Soil"], ans:1, img:"https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"Which part of the plant is found underground and absorbs water?", choices:["Leaf","Flower","Root","Stem"], ans:2 },
    { type:"mcq",     q:"What do seeds need to start growing (germinating)?", choices:["Sunlight only","Water, Soil & Sunlight","Just water","Just soil"], ans:1 },
    { type:"mcq",     q:"Which gas do plants produce during photosynthesis that we need to breathe?", choices:["Carbon dioxide","Nitrogen","Oxygen","Hydrogen"], ans:2 },
    { type:"mcq",     q:"What is the process that plants use to make food from sunlight called?", choices:["Digestion","Respiration","Photosynthesis","Pollination"], ans:2 },
    { type:"mcq",     q:"Which colourful part of the plant attracts bees and butterflies for pollination?", choices:["Root","Stem","Leaf","Flower"], ans:3 },
    { type:"mcq",     q:"A plant that stores water in its thick trunk and survives in hot deserts is a ___.", choices:["Fern","Cactus","Moss","Mushroom"], ans:1 },
    { type:"history", q:"Jan Ingenhousz discovered in 1779 that plants only produce food and release oxygen when exposed to ___.", choices:["Water","Soil","Light","Wind"], ans:2, fact:"In 1779, Dutch scientist Jan Ingenhousz discovered photosynthesis — that plants make food using light. He noticed plants in sunlight produced tiny bubbles (oxygen), but stopped in the dark. A brilliant discovery!" },
    { type:"history", q:"Gregor Mendel, a monk from Austria, discovered the rules of inheritance by studying which plant?", choices:["Roses","Pea plants","Sunflowers","Wheat"], ans:1, fact:"In the 1860s, Gregor Mendel grew thousands of pea plants in his garden and discovered how traits like colour and height are passed from parents to children. He is called the Father of Genetics!" },
    { type:"image",   q:"What type of plant is this tall, yellow flowering plant?", choices:["Rose","Tulip","Sunflower","Daisy"], ans:2, img:"https://images.unsplash.com/photo-1464305795204-6f5bbfc7fb81?w=440&h=270&fit=crop" },
    { type:"image",   q:"This spiky plant stores water inside its trunk and grows in deserts. What is it?", choices:["Fern","Palm tree","Cactus","Bamboo"], ans:2, img:"https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this plant part!", scrambled:"TSOOR", choices:["SHOOT","ROOTS","SEEDS","STEMS"], ans:1 },
    { type:"scramble", q:"Unscramble this plant word!", scrambled:"EDESS", choices:["WEEDS","TREES","SEEDS","LEAFS"], ans:2 },
  ],

  magnet: [
    { type:"mcq",     q:"Which material is attracted to a magnet?", choices:["Plastic","Wood","Iron & Steel","Glass"], ans:2, img:"https://images.unsplash.com/photo-1518770660439-4636190af475?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"How many poles does every magnet have?", choices:["One","Two","Three","Four"], ans:1 },
    { type:"mcq",     q:"What happens when two North poles of magnets face each other?", choices:["They attract","They repel (push away)","They stick together","Nothing happens"], ans:1 },
    { type:"mcq",     q:"Which of these metals is NOT attracted to a magnet?", choices:["Iron","Steel","Aluminium","Nickel"], ans:2 },
    { type:"mcq",     q:"A magnet made by passing electricity through a coil of wire is called an ___.", choices:["Bar magnet","Horseshoe magnet","Electromagnet","Natural magnet"], ans:2 },
    { type:"mcq",     q:"What does the letter N stand for on a magnet?", choices:["Neutral","North","Negative","Normal"], ans:1 },
    { type:"history", q:"William Gilbert (1544–1603) was the first scientist to prove that the Earth itself acts like a giant ___.", choices:["Battery","Magnet","Electric wire","Volcano"], ans:1, fact:"In 1600, William Gilbert published 'De Magnete,' the first great scientific book in English history. He proved Earth is a giant magnet — explaining why compass needles always point North. He also coined the word 'electricity'!" },
    { type:"history", q:"Ancient sailors used lodestones (natural magnets) to navigate. A compass always points towards which direction?", choices:["South","East","West","North"], ans:3, fact:"Over 2,000 years ago, Chinese sailors discovered that lodestone (a natural magnetic rock) always points North. This was the world's first compass! By the 12th century, sailors everywhere used magnetic compasses to navigate oceans." },
    { type:"image",   q:"This instrument uses a magnetic needle to show direction. What is it called?", choices:["Thermometer","Barometer","Compass","Ruler"], ans:2, img:"https://images.unsplash.com/photo-1465101046530-73398c7f28ca?w=440&h=270&fit=crop" },
    { type:"image",   q:"The two coloured ends of this magnet are called what?", choices:["Tips","Poles","Ends","Points"], ans:1, img:"https://images.unsplash.com/photo-1518770660439-4636190af475?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this magnet word!", scrambled:"HNORT", choices:["NORTH","SOUTH","FORCE","STEEL"], ans:0 },
    { type:"scramble", q:"Unscramble this magnet word!", scrambled:"SOELP", choices:["STEEL","POWER","POLES","FORCE"], ans:2 },
  ],

  space: [
    { type:"mcq",     q:"What is the closest star to planet Earth?", choices:["The Moon","Mars","The Sun","Venus"], ans:2, img:"https://images.unsplash.com/photo-1532693322450-2cb5c511067d?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"How many planets are in our Solar System?", choices:["7","8","9","10"], ans:1 },
    { type:"mcq",     q:"Which planet is known as the Red Planet?", choices:["Jupiter","Venus","Saturn","Mars"], ans:3, img:"https://images.unsplash.com/photo-1614728423169-3f65fd722b7e?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"What do we call the curved path a planet takes as it travels around the Sun?", choices:["Revolution","Orbit","Rotation","Axis"], ans:1 },
    { type:"mcq",     q:"Which planet is famous for having beautiful rings around it?", choices:["Jupiter","Mars","Saturn","Neptune"], ans:2 },
    { type:"mcq",     q:"What is a shooting star actually made of?", choices:["A falling star","A meteor burning in the atmosphere","A comet tail","A broken satellite"], ans:1 },
    { type:"mcq",     q:"What is the name of the galaxy our Solar System lives in?", choices:["Andromeda","Black Hole","The Milky Way","Nebula"], ans:2 },
    { type:"history", q:"Neil Armstrong became the first human to walk on the Moon on 20 July ___.", choices:["1959","1969","1979","1989"], ans:1, fact:"On 20 July 1969, Neil Armstrong stepped onto the Moon and said the famous words: 'That's one small step for man, one giant leap for mankind.' The Apollo 11 mission was watched on TV by over 600 million people worldwide!" },
    { type:"history", q:"Galileo Galilei was the first scientist to use a telescope to look at space in 1609. What did he discover around Jupiter?", choices:["Rings","Craters","Four large moons","A giant storm"], ans:2, fact:"In 1609, Galileo pointed his telescope at Jupiter and discovered four large moons orbiting it — proving that not everything in space orbits the Earth. He was put under house arrest for supporting the idea that Earth orbits the Sun!" },
    { type:"image",   q:"Which planet with spectacular rings is shown in this picture?", choices:["Jupiter","Uranus","Neptune","Saturn"], ans:3, img:"https://images.unsplash.com/photo-1630839437035-dac17da580d0?w=440&h=270&fit=crop" },
    { type:"image",   q:"What natural object in our sky is shown in this photo?", choices:["Planet","Comet","Full Moon","Star cluster"], ans:2, img:"https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this space word!", scrambled:"TCEMO", choices:["COMET","ORBIT","STARS","SPACE"], ans:0 },
    { type:"scramble", q:"Unscramble this space word!", scrambled:"RASST", choices:["ORBIT","SPACE","STARS","VENUS"], ans:2 },
  ],

  machines: [
    { type:"mcq",     q:"A sloping ramp used to move heavy things upward is called an ___.", choices:["Lever","Pulley","Inclined Plane","Wedge"], ans:2, img:"https://images.unsplash.com/photo-1581092160562-40aa08e78837?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"A seesaw in the playground is an example of which simple machine?", choices:["Pulley","Lever","Wheel & Axle","Screw"], ans:1 },
    { type:"mcq",     q:"Which simple machine uses a wheel with a groove and a rope to lift heavy loads?", choices:["Lever","Wedge","Pulley","Screw"], ans:2 },
    { type:"mcq",     q:"A knife blade or an axe is an example of which simple machine?", choices:["Screw","Wedge","Pulley","Lever"], ans:1 },
    { type:"mcq",     q:"What do a wheel and axle help us do?", choices:["Cut things","Move things more easily","Lift water","Climb up walls"], ans:1 },
    { type:"mcq",     q:"A screw is actually a twisted version of which other simple machine?", choices:["Lever","Wheel","Wedge","Inclined Plane"], ans:3 },
    { type:"mcq",     q:"Scissors are made from two ___ joined at a pivot point.", choices:["Pulleys","Screws","Levers","Wheels"], ans:2 },
    { type:"history", q:"The ancient Greek scientist Archimedes (287–212 BC) famously said: 'Give me a long enough lever and I can move ___.'", choices:["A mountain","The whole Earth","A building","The sea"], ans:1, fact:"Archimedes was one of the greatest scientists of ancient Greece. He discovered the principles of the lever and pulley. He once used pulleys to help move an entire warship on land by himself! He was so proud he said he could move the Earth with a long enough lever." },
    { type:"history", q:"The wheel is one of the greatest inventions ever. Ancient Mesopotamians (modern-day Iraq) invented it around ___ years ago.", choices:["500","1,000","5,500","10,000"], ans:2, fact:"The wheel was invented in ancient Mesopotamia (modern Iraq) around 3,500 BC — that's about 5,500 years ago! It was first used for pottery spinning, then for carts and chariots. It is considered one of the most important inventions in human history." },
    { type:"image",   q:"A playground slide is an example of which simple machine?", choices:["Lever","Pulley","Wedge","Inclined Plane"], ans:3, img:"https://images.unsplash.com/photo-1575783970733-1aaedde1db74?w=440&h=270&fit=crop" },
    { type:"image",   q:"These interlocking toothed wheels that transfer motion are called ___.", choices:["Screws","Gears","Pulleys","Levers"], ans:1, img:"https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this simple machine name!", scrambled:"RVELE", choices:["WHEEL","LEVER","SCREW","RAMP"], ans:1 },
    { type:"scramble", q:"Unscramble this simple machine name!", scrambled:"LWEHE", choices:["LEVER","WEDGE","WHEEL","SCREW"], ans:2 },
  ],

  weather: [
    { type:"mcq",     q:"What causes rain to fall down from clouds?", choices:["Wind pushing it down","Water droplets becoming too heavy","The Sun heating it","Cold air rising up"], ans:1, img:"https://images.unsplash.com/photo-1504608524841-42584120d693?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"What are clouds actually made of?", choices:["Cotton fibres","Smoke","Tiny water droplets","Floating dust"], ans:2, img:"https://images.unsplash.com/photo-1444930694458-01babf71ab07?w=340&h=185&fit=crop" },
    { type:"mcq",     q:"What is the continuous movement of water between the Earth and sky called?", choices:["Water cycle","Rain cycle","Cloud cycle","Wind cycle"], ans:0 },
    { type:"mcq",     q:"What do we call precipitation that falls as tiny ice crystals?", choices:["Rain","Sleet","Snow","Hail"], ans:2 },
    { type:"mcq",     q:"What causes wind to blow?", choices:["Movement of clouds","Differences in air pressure","The Sun rising","Water evaporating"], ans:1 },
    { type:"mcq",     q:"Which instrument measures the temperature of the air?", choices:["Barometer","Compass","Thermometer","Ruler"], ans:2 },
    { type:"mcq",     q:"A violent spinning column of wind that touches the ground is called a ___.", choices:["Hurricane","Tornado","Blizzard","Monsoon"], ans:1 },
    { type:"history", q:"Gabriel Fahrenheit invented the mercury thermometer in 1714. What does a thermometer measure?", choices:["Wind speed","Air pressure","Temperature","Rainfall"], ans:2, fact:"In 1714, Gabriel Fahrenheit invented the first accurate mercury thermometer and created the Fahrenheit temperature scale. Later in 1742, Anders Celsius invented the Celsius scale. Both scales are still used today!" },
    { type:"history", q:"The first person to accurately predict the weather using science was Robert FitzRoy in 1861. What did he call his predictions?", choices:["Weather maps","Rain reports","Weather forecasts","Storm signals"], ans:2, fact:"In 1861, British admiral Robert FitzRoy made the world's first official weather forecast in a newspaper. He invented the word 'forecast' for weather! He also designed the Fitzroy Barometer still used today to predict storms." },
    { type:"image",   q:"What beautiful natural phenomenon appears after rain when sunlight passes through water droplets?", choices:["Aurora","Lightning","Rainbow","Sunset glow"], ans:2, img:"https://images.unsplash.com/photo-1501630834273-4b5604d2ee31?w=440&h=270&fit=crop" },
    { type:"image",   q:"What type of dramatic weather is shown in this picture?", choices:["Sunny day","Snowstorm","Thunderstorm","Foggy morning"], ans:2, img:"https://images.unsplash.com/photo-1472145246862-b24cf25495bf?w=440&h=270&fit=crop" },
    { type:"scramble", q:"Unscramble this weather word!", scrambled:"DOLCU", choices:["FLOOD","CLOUD","STORM","FROST"], ans:1 },
    { type:"scramble", q:"Unscramble this weather word!", scrambled:"MORTS", choices:["FROST","FLOOD","SLEET","STORM"], ans:3 },
  ],
};

// ── Letter Tile ───────────────────────────────────────────────────────────────
function Tile({ ch, color }) {
  return (
    <div style={{ width:42,height:52,borderRadius:8,background:color,color:"#fff",display:"flex",alignItems:"center",justifyContent:"center",fontSize:22,fontWeight:900,fontFamily:"Georgia,serif",boxShadow:`0 4px 0 rgba(0,0,0,0.28),0 6px 14px rgba(0,0,0,0.12)`,userSelect:"none" }}>
      {ch}
    </div>
  );
}

// ── Badge ─────────────────────────────────────────────────────────────────────
function Badge({ score, total }) {
  const p = score/total;
  const cfg = p>=0.85
    ? { grad:"linear-gradient(135deg,#FFD700,#FF8C00)", label:"Gold Star Explorer!", glow:"rgba(255,195,0,0.5)" }
    : p>=0.65
    ? { grad:"linear-gradient(135deg,#C0C0C0,#707070)", label:"Silver Explorer!", glow:"rgba(130,130,130,0.4)" }
    : { grad:"linear-gradient(135deg,#CD7F32,#8B4513)", label:"Bronze Explorer!", glow:"rgba(150,80,20,0.35)" };
  return (
    <div style={{ textAlign:"center",marginBottom:4 }}>
      <div style={{ width:86,height:86,borderRadius:"50%",background:cfg.grad,display:"flex",alignItems:"center",justifyContent:"center",margin:"0 auto 10px",boxShadow:`0 6px 24px ${cfg.glow}` }}>
        <svg width="44" height="44" viewBox="0 0 48 48" fill="white"><path d="M24 4L29.5 17H44L32.5 26L37 40L24 32L11 40L15.5 26L4 17H18.5Z"/></svg>
      </div>
      <div style={{ fontFamily:"Georgia,serif",fontWeight:800,fontSize:17,color:"#1A2E4A" }}>{cfg.label}</div>
    </div>
  );
}

// ── Main ──────────────────────────────────────────────────────────────────────
export default function ScienceGame() {
  const [screen,   setScreen]   = useState("home");
  const [topic,    setTopic]    = useState(null);
  const [qIdx,     setQIdx]     = useState(0);
  const [selected, setSelected] = useState(null);
  const [score,    setScore]    = useState(0);
  const [answered, setAnswered] = useState(false);
  const [imgErr,   setImgErr]   = useState({});
  const [log,      setLog]      = useState([]);

  const qs  = topic ? QUESTIONS[topic.id] : [];
  const cur = qs[qIdx];

  function go(t) {
    setTopic(t); setQIdx(0); setSelected(null);
    setScore(0); setAnswered(false); setImgErr({}); setLog([]);
    setScreen("quiz");
  }

  function pick(i) {
    if (answered) return;
    setSelected(i); setAnswered(true);
    const ok = i === cur.ans;
    if (ok) setScore(s => s+1);
    setLog(l => [...l, { ok, type:cur.type }]);
  }

  function next() {
    if (qIdx+1 < qs.length) { setQIdx(x=>x+1); setSelected(null); setAnswered(false); }
    else setScreen("result");
  }

  // ── HOME ──────────────────────────────────────────────────────────────────
  if (screen === "home") return (
    <div style={{ minHeight:"100vh", background:"#F3F0EB", fontFamily:"'Trebuchet MS',Georgia,serif" }}>
      <div style={{ background:"linear-gradient(160deg,#0C1F35,#164066,#1B4F72)", padding:"36px 22px 28px", textAlign:"center", position:"relative", overflow:"hidden" }}>
        {[...Array(24)].map((_,i)=>(
          <div key={i} style={{ position:"absolute", width:i%4===0?3:2, height:i%4===0?3:2, borderRadius:"50%", background:"white", opacity:0.12+((i*7)%5)*0.09, top:`${(i*43+5)%90}%`, left:`${(i*61+9)%96}%` }} />
        ))}
        <div style={{ display:"inline-flex",alignItems:"center",gap:8,background:"rgba(255,210,60,0.14)",border:"1px solid rgba(255,210,60,0.32)",borderRadius:30,padding:"5px 16px",marginBottom:14 }}>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="#FFD700"><path d="M12 2L14.5 9H22L16 13.5L18.5 21L12 17L5.5 21L8 13.5L2 9H9.5Z"/></svg>
          <span style={{ color:"#FFD700",fontWeight:700,fontSize:12,letterSpacing:1.2,textTransform:"uppercase" }}>Science Explorer</span>
        </div>
        <h1 style={{ color:"white",margin:"0 0 6px",fontSize:"clamp(22px,5vw,36px)",fontWeight:900,textShadow:"0 2px 14px rgba(0,0,0,0.4)" }}>The Big Science Quiz</h1>
        <p style={{ color:"rgba(255,255,255,0.62)",margin:"0 0 18px",fontSize:14 }}>10+ questions per topic — Multiple Choice · Spot-It · Spelling · History</p>
        <div style={{ display:"flex",gap:8,justifyContent:"center",flexWrap:"wrap" }}>
          {Object.entries(TYPE_CFG).map(([k,v])=>(
            <span key={k} style={{ background:v.bg,color:v.color,border:`1px solid ${v.border}`,borderRadius:20,padding:"3px 11px",fontSize:11,fontWeight:700 }}>{v.label}</span>
          ))}
        </div>
      </div>

      <div style={{ maxWidth:900,margin:"0 auto",padding:"28px 16px",display:"grid",gridTemplateColumns:"repeat(auto-fill,minmax(188px,1fr))",gap:15 }}>
        {TOPICS.map(t=>(
          <button key={t.id} onClick={()=>go(t)} style={{ all:"unset",cursor:"pointer",background:"white",borderRadius:16,overflow:"hidden",boxShadow:"0 2px 10px rgba(0,0,0,0.07)",border:"2px solid transparent",transition:"all 0.17s ease",display:"block" }}
            onMouseEnter={e=>{e.currentTarget.style.transform="translateY(-5px)";e.currentTarget.style.boxShadow=`0 10px 26px rgba(0,0,0,0.13)`;e.currentTarget.style.borderColor=t.color;}}
            onMouseLeave={e=>{e.currentTarget.style.transform="translateY(0)";e.currentTarget.style.boxShadow="0 2px 10px rgba(0,0,0,0.07)";e.currentTarget.style.borderColor="transparent";}}
          >
            <div style={{ position:"relative",height:94,overflow:"hidden",background:t.bg }}>
              <img src={t.img} alt={t.title} style={{ width:"100%",height:"100%",objectFit:"cover",opacity:.87 }} onError={e=>e.target.style.display="none"} />
              <div style={{ position:"absolute",inset:0,background:`linear-gradient(to bottom,transparent 25%,${t.color}CC)` }} />
              <div style={{ position:"absolute",top:8,right:8,width:30,height:30,borderRadius:"50%",background:"white",display:"flex",alignItems:"center",justifyContent:"center",color:t.color,boxShadow:"0 2px 8px rgba(0,0,0,0.18)" }}>
                {t.icon}
              </div>
            </div>
            <div style={{ padding:"10px 13px 13px" }}>
              <div style={{ fontWeight:800,fontSize:13.5,color:"#1A2E4A" }}>{t.title}</div>
              <div style={{ fontSize:11.5,color:"#999",marginTop:2 }}>{QUESTIONS[t.id].length} questions</div>
              <div style={{ marginTop:7,display:"flex",gap:4,flexWrap:"wrap" }}>
                {["mcq","image","scramble","history"].filter(tp=>QUESTIONS[t.id].some(q=>q.type===tp)).map(tp=>(
                  <span key={tp} style={{ background:TYPE_CFG[tp].bg,color:TYPE_CFG[tp].color,fontSize:9,fontWeight:700,padding:"2px 6px",borderRadius:10,border:`1px solid ${TYPE_CFG[tp].border}` }}>
                    {tp==="mcq"?"MCQ":tp==="image"?"Spot It":tp==="scramble"?"Spell It":"History"}
                  </span>
                ))}
              </div>
            </div>
          </button>
        ))}
      </div>
      <div style={{ textAlign:"center",paddingBottom:28,color:"#BBB",fontSize:13 }}>Pick any topic above to begin your adventure</div>
    </div>
  );

  // ── QUIZ ──────────────────────────────────────────────────────────────────
  if (screen === "quiz" && cur) {
    const tc = TYPE_CFG[cur.type] || TYPE_CFG.mcq;
    const isImg = cur.type === "image";
    const isSc  = cur.type === "scramble";

    return (
      <div style={{ minHeight:"100vh",background:"#F3F0EB",fontFamily:"'Trebuchet MS',Georgia,serif" }}>
        {/* Topbar */}
        <div style={{ background:"white",borderBottom:`3px solid ${topic.color}`,padding:"10px 18px",display:"flex",alignItems:"center",gap:10 }}>
          <button onClick={()=>setScreen("home")} style={{ all:"unset",cursor:"pointer",display:"flex",alignItems:"center",gap:5,color:"#666",fontSize:13,fontWeight:700 }}>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round"><path d="M19 12H5M12 5l-7 7 7 7"/></svg>Topics
          </button>
          <div style={{ flex:1 }}>
            <div style={{ height:7,background:"#EEE",borderRadius:4,overflow:"hidden" }}>
              <div style={{ height:"100%",borderRadius:4,background:`linear-gradient(90deg,${topic.color},${topic.color}88)`,width:`${(qIdx/qs.length)*100}%`,transition:"width 0.45s ease" }} />
            </div>
          </div>
          <span style={{ background:topic.bg,color:topic.color,fontWeight:700,fontSize:12,padding:"3px 10px",borderRadius:20,border:`1px solid ${topic.color}30`,whiteSpace:"nowrap" }}>{qIdx+1}/{qs.length}</span>
          <span style={{ display:"flex",alignItems:"center",gap:4,background:"#FFFBEA",color:"#B45309",fontWeight:700,fontSize:12,padding:"3px 10px",borderRadius:20 }}>
            <svg width="11" height="11" viewBox="0 0 24 24" fill="#B45309"><path d="M12 2L14.5 9H22L16 13.5L18.5 21L12 17L5.5 21L8 13.5L2 9H9.5Z"/></svg>{score}
          </span>
        </div>

        <div style={{ maxWidth:650,margin:"0 auto",padding:"22px 18px 36px" }}>
          {/* Type chips */}
          <div style={{ display:"flex",gap:7,marginBottom:14,flexWrap:"wrap" }}>
            <span style={{ background:tc.bg,color:tc.color,border:`1px solid ${tc.border}`,borderRadius:20,padding:"4px 12px",fontWeight:700,fontSize:11,textTransform:"uppercase",letterSpacing:.7 }}>{tc.label}</span>
            <span style={{ background:topic.bg,color:topic.color,border:`1px solid ${topic.color}28`,borderRadius:20,padding:"4px 12px",fontWeight:700,fontSize:11,textTransform:"uppercase",letterSpacing:.7 }}>{topic.title}</span>
          </div>

          <h2 style={{ color:"#0D1D2F",fontSize:"clamp(15px,2.7vw,20px)",fontWeight:800,marginBottom:18,lineHeight:1.42 }}>{cur.q}</h2>

          {/* Large image (Spot It) */}
          {isImg && !imgErr[qIdx] && (
            <div style={{ borderRadius:16,overflow:"hidden",marginBottom:20,height:230,background:topic.bg,border:`2px solid ${topic.color}22`,boxShadow:"0 4px 20px rgba(0,0,0,0.1)" }}>
              <img src={cur.img} alt="identify" style={{ width:"100%",height:"100%",objectFit:"cover" }} onError={()=>setImgErr(e=>({...e,[qIdx]:true}))} />
            </div>
          )}

          {/* Small image (MCQ / history) */}
          {!isImg && !isSc && cur.img && !imgErr[qIdx] && (
            <div style={{ borderRadius:13,overflow:"hidden",marginBottom:18,height:158,background:topic.bg,border:`2px solid ${topic.color}18` }}>
              <img src={cur.img} alt="question" style={{ width:"100%",height:"100%",objectFit:"cover" }} onError={()=>setImgErr(e=>({...e,[qIdx]:true}))} />
            </div>
          )}

          {/* Scramble tiles */}
          {isSc && (
            <div style={{ background:tc.bg,border:`2px dashed ${tc.border}`,borderRadius:16,padding:"18px 20px",marginBottom:20,textAlign:"center" }}>
              <div style={{ fontSize:11,fontWeight:700,color:tc.color,textTransform:"uppercase",letterSpacing:1,marginBottom:13 }}>Unscramble the Letters</div>
              <div style={{ display:"flex",gap:7,justifyContent:"center",flexWrap:"wrap" }}>
                {cur.scrambled.split("").map((ch,i)=><Tile key={i} ch={ch} color={topic.color} />)}
              </div>
              {answered && (
                <div style={{ marginTop:14,fontSize:13,fontWeight:700,color:topic.color }}>
                  Answer: <span style={{ background:topic.color,color:"white",padding:"2px 10px",borderRadius:12,marginLeft:4 }}>{cur.choices[cur.ans]}</span>
                </div>
              )}
            </div>
          )}

          {/* Choices */}
          <div style={{ display:"grid",gridTemplateColumns:"1fr 1fr",gap:10 }}>
            {cur.choices.map((c,i)=>{
              let bg="white",br="#E5E7EB",clr="#0D1D2F",icon=null;
              if (answered) {
                if (i===cur.ans) { bg="#F0FDF4"; br="#22C55E"; clr="#15803D"; icon=<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#22C55E" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"><path d="M20 6L9 17l-5-5"/></svg>; }
                else if (i===selected) { bg="#FFF1F0"; br="#EF4444"; clr="#DC2626"; icon=<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#EF4444" strokeWidth="3" strokeLinecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>; }
              }
              return (
                <button key={i} onClick={()=>pick(i)} style={{ all:"unset",cursor:answered?"default":"pointer",background:bg,border:`2px solid ${br}`,borderRadius:12,padding:"12px 14px",display:"flex",alignItems:"center",gap:9,color:clr,fontWeight:600,fontSize:13,transition:"all 0.12s ease",boxShadow:answered&&i===cur.ans?"0 0 0 3px #86EFAC48":"none" }}
                  onMouseEnter={e=>{if(!answered)e.currentTarget.style.borderColor=topic.color;}}
                  onMouseLeave={e=>{if(!answered)e.currentTarget.style.borderColor="#E5E7EB";}}
                >
                  <span style={{ minWidth:24,height:24,borderRadius:"50%",background:answered&&i===cur.ans?"#22C55E":answered&&i===selected?"#EF4444":`${topic.color}18`,color:answered&&(i===cur.ans||i===selected)?"white":topic.color,display:"flex",alignItems:"center",justifyContent:"center",fontWeight:800,fontSize:11,flexShrink:0 }}>
                    {answered?(icon||String.fromCharCode(65+i)):String.fromCharCode(65+i)}
                  </span>
                  {c}
                </button>
              );
            })}
          </div>

          {/* Feedback */}
          {answered && (
            <div style={{ marginTop:16 }}>
              <div style={{ padding:"11px 16px",borderRadius:11,background:selected===cur.ans?"#F0FDF4":"#FFF1F0",border:`1px solid ${selected===cur.ans?"#86EFAC":"#FECACA"}`,color:selected===cur.ans?"#15803D":"#DC2626",fontWeight:700,fontSize:13,display:"flex",alignItems:"center",gap:8,marginBottom:cur.fact?12:14 }}>
                {selected===cur.ans
                  ? <><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><path d="M20 6L9 17l-5-5"/></svg>Excellent! That is correct!</>
                  : <><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round"><path d="M18 6L6 18M6 6l12 12"/></svg>Correct answer: <strong style={{ marginLeft:4 }}>{cur.choices[cur.ans]}</strong></>
                }
              </div>

              {cur.fact && (
                <div style={{ padding:"14px 16px",borderRadius:13,background:"linear-gradient(135deg,#FDF4FF,#F3E8FF)",border:"1px solid #D8B4FE",marginBottom:14 }}>
                  <div style={{ display:"flex",gap:10,alignItems:"flex-start" }}>
                    <div style={{ width:30,height:30,borderRadius:"50%",background:"#7E22CE",display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0,marginTop:1 }}>
                      <svg width="14" height="14" viewBox="0 0 24 24" fill="white"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
                    </div>
                    <div>
                      <div style={{ fontWeight:800,fontSize:11,color:"#7E22CE",textTransform:"uppercase",letterSpacing:.9,marginBottom:5 }}>Did You Know?</div>
                      <div style={{ fontSize:13,color:"#4B0082",lineHeight:1.55 }}>{cur.fact}</div>
                    </div>
                  </div>
                </div>
              )}

              <button onClick={next} style={{ all:"unset",cursor:"pointer",background:topic.color,color:"white",fontWeight:800,fontSize:14,padding:"13px 28px",borderRadius:12,display:"flex",alignItems:"center",gap:8,width:"100%",justifyContent:"center",boxShadow:`0 4px 18px ${topic.color}50` }}>
                {qIdx+1 < qs.length ? "Next Question" : "See My Results"}
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              </button>
            </div>
          )}

          {/* Dot progress */}
          <div style={{ display:"flex",gap:5,justifyContent:"center",marginTop:22,flexWrap:"wrap" }}>
            {qs.map((_,i)=>(
              <div key={i} style={{ width:i===qIdx?22:8,height:8,borderRadius:4,background:i<log.length?(log[i].ok?"#22C55E":"#EF4444"):i===qIdx?topic.color:"#DDD",transition:"all 0.25s ease" }} />
            ))}
          </div>
        </div>
      </div>
    );
  }

  // ── RESULT ────────────────────────────────────────────────────────────────
  if (screen === "result") {
    const byType = {};
    log.forEach(h=>{
      if (!byType[h.type]) byType[h.type]={ total:0, correct:0 };
      byType[h.type].total++;
      if (h.ok) byType[h.type].correct++;
    });

    return (
      <div style={{ minHeight:"100vh",background:"#F3F0EB",fontFamily:"'Trebuchet MS',Georgia,serif",display:"flex",flexDirection:"column",alignItems:"center",justifyContent:"center",padding:"26px 16px" }}>
        <div style={{ background:"white",borderRadius:24,padding:"36px 30px",maxWidth:440,width:"100%",boxShadow:"0 8px 40px rgba(0,0,0,0.1)",border:`3px solid ${topic.color}22`,textAlign:"center" }}>
          <div style={{ color:"#AAA",fontWeight:700,fontSize:11,textTransform:"uppercase",letterSpacing:1.3,marginBottom:6 }}>{topic.title} — Quiz Complete</div>
          <Badge score={score} total={qs.length} />

          <div style={{ margin:"20px 0 16px" }}>
            <div style={{ fontSize:11,color:"#AAA",marginBottom:3 }}>Your Score</div>
            <div style={{ fontSize:50,fontWeight:900,color:topic.color,lineHeight:1 }}>
              {score}<span style={{ fontSize:22,color:"#CCC" }}>/{qs.length}</span>
            </div>
            <div style={{ background:"#F3F4F6",borderRadius:50,height:8,overflow:"hidden",margin:"12px 0 8px" }}>
              <div style={{ height:"100%",width:`${(score/qs.length)*100}%`,background:`linear-gradient(90deg,${topic.color},${topic.color}80)`,borderRadius:50,transition:"width 1.1s ease" }} />
            </div>
            <div style={{ fontSize:13,color:"#666" }}>
              {score===qs.length?"Perfect! You are a true Science Explorer!":score>=Math.round(qs.length*.8)?"Brilliant! Almost perfect!":score>=Math.round(qs.length*.6)?"Great effort! Keep learning!":"Good try — review and try again!"}
            </div>
          </div>

          {/* Breakdown by type */}
          <div style={{ background:"#F8F7F5",borderRadius:14,padding:"14px 16px",marginBottom:20 }}>
            <div style={{ fontSize:10,fontWeight:700,color:"#BBB",textTransform:"uppercase",letterSpacing:1,marginBottom:10 }}>By Question Type</div>
            {Object.entries(byType).map(([tp, d])=>{
              const tc2 = TYPE_CFG[tp]||TYPE_CFG.mcq;
              const pct = d.correct/d.total;
              return (
                <div key={tp} style={{ display:"flex",alignItems:"center",gap:9,marginBottom:8 }}>
                  <span style={{ width:72,fontSize:10,fontWeight:700,color:tc2.color,background:tc2.bg,border:`1px solid ${tc2.border}`,borderRadius:10,padding:"2px 6px",textAlign:"center",whiteSpace:"nowrap" }}>{tc2.label.split(" ")[0]}</span>
                  <div style={{ flex:1,height:7,background:"#E5E7EB",borderRadius:4,overflow:"hidden" }}>
                    <div style={{ height:"100%",width:`${pct*100}%`,background:pct>0.7?"#22C55E":pct>0.4?"#F59E0B":"#EF4444",borderRadius:4,transition:"width 1s ease" }} />
                  </div>
                  <span style={{ fontSize:12,fontWeight:700,color:"#555",minWidth:28 }}>{d.correct}/{d.total}</span>
                </div>
              );
            })}
          </div>

          <div style={{ display:"flex",gap:10 }}>
            <button onClick={()=>go(topic)} style={{ all:"unset",cursor:"pointer",flex:1,background:topic.bg,color:topic.color,fontWeight:800,fontSize:13,padding:"13px",borderRadius:12,border:`2px solid ${topic.color}38`,textAlign:"center" }}>Try Again</button>
            <button onClick={()=>setScreen("home")} style={{ all:"unset",cursor:"pointer",flex:1,background:topic.color,color:"white",fontWeight:800,fontSize:13,padding:"13px",borderRadius:12,textAlign:"center",boxShadow:`0 4px 16px ${topic.color}48` }}>All Topics</button>
          </div>
        </div>
      </div>
    );
  }

  return null;
}
