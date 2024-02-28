import streamlit as st
from openai import OpenAI
from common import voiceToText, textToVoice

user_prompt = """
Bat woke up.
He flew out of his cave.,"I want bugs!"
Bat said.,"I will find bugs.
And I will eat them!",Bat flew up in the sky.,Bat flew over houses.
He flew over trees.,He found some big bugs.
He found some little bugs.,He ate and ate and ate.
He flew and flew and flew.,Bat was happy.
"It's time to go home and sleep!",But now it was very dark.
"Where is home?" Bat said.,A big wind came up.
A lot of rain came down.,Bat was far from home.,"I am wet," said Bat.
"And I am lost.","I must find a dry place.
I must find a safe place.",So Bat flew and flew.
He looked all around.,The wind was strong.
The rain was wet.,Bat did not see a dry place.
He did not see a safe place.,Then Bat saw something.
It was big and red.,It was a barn!,Bat flew to the roof.
He went over the side.,He hung by his toes.
He looked for a way to get in.,Then Bat saw a hole.
It was little.,But so was Bat.,Bat went into the hole.,The barn was dry.
But was it safe?,Bat did not know.
He looked around.,The barn was big.
And Bat was little.,So maybe it was safe.,Bat hung by his feet.
He went to sleep.,The next day Bat woke up.
It was still raining.,Bat looked down.
He saw a brown cow.,He saw a yellow cat.
He heard a pig.,But there were no bats.,Did Cow and Cat and Pig like bats?
Could they be his friends?,"I will wait and see," Bat said.,The sky was not blue.
It was gray.,Cat woke up.                      	
"Look at that!" she said.,Little drops came down.
Big drops came down.,"Go away, rain," said Cat.
"I want to play.","Go away, rain," said Cow.
"I want to see the sun.","Go away, rain," said Pig.
"I want to eat.","I don't like rain," said Cat.
"I don't like rain," said Cow.,"<em>We</em> don't like rain," said Pig.,But the rain came down.          
The rain did not stop.,The three friends stayed in the barn.
They did not go out.,Pig said, "When will the rain go away?" 
Cow said, "What can we do?","I know!" said Cat.
"We can play in the barn.","Play what?" said Pig. 
"We can play What Is It?" said Cat.,"I see something yellow," said Cat.
"What is it?",Pig and Cow looked around.,"Is it hay?" said Pig. 
"No, it is not hay," said Cat.,"Is it the light?" said Cow.
"No, it is not the light," said Cat.,"Is it the boot?" said Pig.
"Yes! It is the yellow boot!" said Cat.,"Now, Pig," said Cat.
"You say what you see!","I see something blue," said Pig.     
"It is something new.",Cow and Cat looked around.
But they did not see anything.,"If you guess," said Pig,
"I will take you for a ride!",Cat looked all over. 
Cow looked all over.,They did not see anything blue.
They did not see anything new.,Then Cat saw something.
"There it is!" she said.,"It is blue and it is new!
It is a wagon!","I am too big to ride," said Cow .
"But I can pull!",Cow pulled and pulled.
Then Pig pulled and pulled.,The three friends went round and round.,"Look!" said Cat. "Over there!		
I see something blue again!","I see something yellow," said Pig.
"I see something red and green," said Cow.,The three friends went out of the barn.		 
They looked up.,The sky was blue.
And there was a rainbow!,Bat liked the barn.
He liked Cow and Pig and Cat.,He wanted to play with them.,So Bat flew to Cow.
"Will you play with me?" he said.,"No!" said Cow. "I do not like bats. 
Please go away!",So Bat left.,Bat flew to Pig.
"Will you play with me?" said Bat.,"No," said Pig. "I do not like bats.
Please go away!",So Bat left.,Bat flew to Cat.
"Will you play with me?","No," said Cat. "I do not like bats.
Please go away.",So Bat left.,No one wanted to play with Bat.
He was all alone.,Bat was sad.
He liked the barn.,He liked Cow and Pig and Cat.
But they did not like Bat.,They did not want to play with him.,"If I am a cow," said Bat,
"Cow will play with me.","Cow will be my friend.","If I am a pig," said Bat,
"Pig will play with me.","Pig will be my friend.","If I am a cat," said Bat,
"Cat will play with me.","Cat will be my friend.","I will think and think," said Bat.,"I will think of a way 
to be a pig, a cow, or a cat.","And soon I will have new friends!",At last Bat knew what to do.
He flew back to Cow.,"I am brown," said Bat.
"Just like you.","Oh!" said Cow. 
"Then I can be your friend!",Bat flew to Pig.
"I like to eat. Just like you," said Bat.,"Oh!" said Pig. 
"Then I can be your friend!",Bat flew to Cat.
"I like to sleep," said Bat. "Just like you.","Oh!" said Cat. 
"Then I can be your friend.",Bat was happy.
He flew round and round.,"I like it here!" he said.,"Welcome to the barn!" said Cow and
Cat and Pig.,Bat had three new friends.
Bat had a new home.,The sun was up.
The sky was blue.,Cat said, "I can jump.
I can jump over the gate.,Watch me jump!",Bat said, "I can fly.
I can fly over the tree.,Watch me fly!",Cow said, "I can walk.
I can walk around the well.,And I can make a wish!","A wish?" said Bat.
"I want to make a wish!","So do I!" said Cat.,Cow said, "You can make a wish.
I will help you.",Cat and Bat went to the well.
"How do we make a wish?" said Cat.,"Watch me," said Cow.
"I will show you what to do!","Tell us, Cow," said Cat.
"Tell us how to make a wish.",Cow said, "Walk around the well three times.
Say, 'Please, please, pretty please.'",Cow went around the well.
She said, "Please, please, pretty please.",Then Cat went around the well.
She said, "Please, please, pretty please" too.,Then Bat went around the well.
He said, "Please, please, pretty please" too.,Cow said, "Now sing to the well.
You must sing your wish.",Cat sang, "I'm tired of this farm.
I think it is a bore.,I want to see new places 
I've never seen before.","I can't sing," said Bat.
"I will not get my wish.",Cow said, "Just try, Bat."
But Bat was too sad.,"It will not work," he said.
"I must fly away now.",Bat flew away.
He did not know how to sing.,He heard Red Bird sing.,He tried to sing like Red Bird.
But he was not good at all.,He tried to sing like Cat.
But he was not good at all.,Bat sang and sang.
He tried and tried.,He wanted to sing his wish again.,Cat was still at the well.
But she sang a new song.,"Forget the wish I made before. 
This is one that I want more.
Please help Bat sing.",And Bat did sing!,Bat sang to the well.
"Give Cat new things to see.",Then Cat and Bat and Cow went away.
They saw many new things.,And they sang!,Bat saw something brown.
He went to tell Cow.,"I saw something brown," said Bat.
"Is it a hat?" said Cow.,"It is not a hat," said Bat.
He went to Pig.,"I saw something brown and hard," said Bat.
 "It's not a hat.","Is it a box?" said Pig.
"A box is brown and hard.","It is not a box," said Bat.
Bat went to Cat.,"I saw something in the barn," said Bat.
"It is brown and hard and small.","It is not a hat or a box.","Is it a rock?" said Cat.
"A rock is brown and hard.","A rock can be small too," Cat said.
"It is not a rock," said Bat.,Bat went back to the barn.
What was this thing?,"Come look at this thing," said Bat.,"It is not a hat. It is not a box.
It is not a rock," said Bat.,"It is brown. It is hard. 
And it is small," said Bat. 
"Can you tell me what it is?",They all went into the barn.
"The thing is over there," said Bat.,They went to the spot.
They looked at the thing.,"You said the thing is brown," said Cow.
"This thing is not brown.","You said the thing is hard.
This thing is not hard," said Pig.,"You said the thing is small," said Cat.
"You are right. 
This thing is very small.",Bat flew over.
He looked at the thing again.,"But where is the thing I saw?" said Bat.
"I do not see it now.",Bat looked and looked.,The thing that was brown and hard
was not there.,This thing was yellow.
This thing was soft.,The thing made a sound.
It said, "Cheep! Cheep!",Cat said, "Bat, what is this thing?","It is a chick!" said Bat.
"It is a soft, yellow chick!","I found it," said Bat.
"So it is mine. Right?","No," said Cow.
"The chick must go to its mother.","But you have something too," said Cow.
"What do I have?" said Bat.,"You have a story," said Cow.
"It is about the thing in the barn.
You can tell this story to your friends.",And that is what Bat did.,Farmer came to the barn.
His phone rang.,"Hello?" said Farmer.
"Yes. The watchdog is coming today.",Farmer talked and talked.
Cow moved closer to hear.,Then Farmer left the barn.,"Moo!" cried Cow.
"Moo! Moo! Moo!",Pig ran from his pen.
Cat and Bat came too.,"I have news!" said Cow.
"What is it?" asked Pig.,"It is BIG news!" said Cow.
"A dog is coming to the farm!","A DOG?" cried Cat.
"Yes," said Cow. "A dog.","But dogs bark," said Cat.
"And they chase cats!","Dogs do not like cats!" said Cat.
"And cats do not like dogs!","Is Dog big or little?" asked Pig.
"I think he's big," said Cow.,"What will Dog do?" Bat asked.
"He is a watchdog," said Cow.,"Dog will watch the farm.
He will keep it safe," said Cow.,"He will not keep <em>me</em> safe," said Cat.
"Dogs do not like cats.","Some dogs like cats," said Cow.
"No, they don't!" said Cat.,Soon Cat left the barn.
She saw a truck.,The truck came closer and closer.
Then Dog got out!,"Woof! Woof!" said Dog.
"I must hide!" said Cat.,"I must hide now!"
Cat looked around.,She saw a tall tree.
Cat ran to the top.,"This is a good place," said Cat.
"Dog will not get me here!",Dog went into the barn.
"Who lives here?" he asked.,"I live here," said Cow. 
"Bat and Pig and Cat do too.","Where is Cat?" asked Dog.
"I don't know," said Cow.,Cat was way up high.
She held on tight. 
"Help!" she cried.,"Cat!" called Pig.
"Where are you?" said Cow.,"I'm stuck in the tree!" cried Cat.
"I can't get down!","I can help!" said Dog.
He ran to the house.,"Woof! Woof!" said Dog.
He barked and barked.,At last Farmer came out.
Dog ran back to the tree.
Farmer ran too.,Farmer knew what to do.
He got Cat down.,Everyone cheered.
"Some dogs <em>do</em> like cats," said Cat.,Pig went into the barn.,He put on his cape.
He put on his mask.,Now he was Super Pig!
"I am off to do good things!","Ta-da! Cow, I am Super Pig! 
I am here to help you!","Oh!" said Cow. "Hello, Pig!
I like your cape!","I am not Pig. I am Super Pig!
How can I help you, Cow?","I'm just eating grass," said Cow.
"I don't need any help.","Please," said Pig.  
"There must be something I can do.",Cow thought and thought.
"I like clover," she said at last.,"But there are bees on the clover.
Can you chase the bees away?","Of course I can!" said Super Pig.,Pig ran to the clover.
He oinked at the bees.,The bees buzzed.
Pig oinked some more.,The bees buzzed some more.
Pig blew on them.,The bees buzzed and buzzed.
Pig huffed and puffed.,He oinked and blew.
He ran around the bees.,The bees buzzed around Pig.
They landed on his face.,Then one big bee stung Pig.
It stung him right on his nose!,"Ouch! Ouch! Ouch!" said Pig.,"Oh no, Pig!" said Cow. 
"Did that hurt?","Yes!" said Pig. 
He ran to the pond.
He put his nose in the mud.,"Thank you, Super Pig!" said Cow.
"All the bees are gone.
And the clover is very good!",Pig's nose felt better.
He went to do more good things.,Cat was on the roof.
She could not get down.,"I will help you!" said Pig.
"Jump onto me.",So Cat jumped.
But her claws dug into Pig's back.,"Ouch! Ouch! Ouch!" yelled Pig.,"Sorry, Pig!" Cat said.
"But thanks for helping me.",Pig ran back to the pond.,Cat ran with him.
Pig rolled in the cool, wet mud.,"My nose hurts," said Pig.
"My back hurts.
I am not a very good Super Pig.","But you are a super friend," said Cow.,"Yes," said Cat.
"And that is much, much better!","Play with me, Pig!" said Bat.
"Okay," said Pig.,"Close your eyes," said Bat.
"And count to ten.","I will hide," said Bat.
"You will seek.
You will try to find me!",Pig closed his eyes.
He began to count.
"One, two, three . . .","What are you doing, Pig?" asked Cat.
"I'm playing with Bat," said Pig.
"We are playing hide-and-seek.","Can I play?" asked Cat.
"Yes," said Pig.,Cat went to hide.
Pig started to count again.
"One, two, three . . .","Hide-and-seek!" said Dog.
"Can I play?","Yes," said Pig. 
Pig began to count again.
"One, two, three, four . . .","I want to play too!" said Cow.
Cow hid.
Pig counted.,"Eight, nine, ten! 
Here I come!" said Pig.,Pig looked for his friends.
They were not at the pond.,They were not in the barn. 
They were not behind the barn.,They were not in the field. 
They were not at the house.,Where were Pig's friends?
Pig did not see them anywhere.,"Oh!" said Pig.
"They are playing a trick!
They are playing a trick on me!","They are mean!" said Pig.
"I do not like this game anymore!",Pig was very sad.
But he knew what to do.,"I will eat something," said Pig.
"Then I will feel better.",So Pig ate and ate. 
He ate some more.,Now Pig was very full. 
But he was still sad.,Then Pig saw something.
It was something shiny!,Pig looked at the shiny thing.
It was a pair of glasses!,Pig picked up the glasses.
He put them on.,"Wow!" said Pig.
"Now I can see everything!",Pig looked all around.
"Maybe my friends are <em>not</em> tricking me!",Pig ran back to the barn.
"I see you, Bat!" he said.,Pig ran back to the pond.
"I see you, Dog!" he said.,Pig ran behind the barn.
"I see you, Cow!" he said.,Pig ran to the field.
"I see you, Cat!" he said.,"I can see everything!" Pig cried. 
"Let's play hide-and-seek again!","Okay," said Cow. "We will hide.
And you will look for us.","No," said Pig.
"This time I will hide.
And you will look for me!","Woof! Woof!" said Dog.
"Woof! Woof! Woof!","That is not Dog's happy bark," said Cow.
"Something is wrong!",Pig and Cat ran outside.
They ran to Red Bird's tree.
There was Dog.,"I saw something," said Dog.
"It was black.
It was big!","How big was it?" asked Cat.
"It was bigger than Farmer!" said Dog.
"And it ate Red Bird's food!","It's a monster," said Cat.             
"A hungry monster!" said Pig.,"I barked and barked," said Dog.
"I barked until it ran away.","Will it come back?" asked Pig.
"Will it eat us?" asked Cat.,"No," said Dog.
"I will watch the farm.
I will keep us safe.","We must tell Cow," said Cat.
"We must tell her about the monster!","I will stay here," said Dog.
"I will watch the farm.",Cat and Pig ran back to the barn.
"Dog saw a monster!" said Pig.,"It was black!" said Cat.
"It was big!" said Pig.,"What did it do?" Cow asked.
"It ate Red Bird's food!" said Pig.,"Oh!" said Cow. "That's just the bear.
The bear came last year too.","Dog barked," said Cat.
"And it ran away. 
But it might come back!","Yes," said Cow.
"It might come back.
But I have a plan.","What is your plan?" asked Pig.
"We will look for blueberries!" said Cow.,Cow looked for blueberries.
Pig, Cat, and Bat looked too.,"I see some!" said Bat.
"We must pick them," said Cow.,The friends picked blueberries.
They put them on the path.
Then they told Dog about the plan.,Dog was at Red Bird's tree.
He watched for the bear.,At last Dog saw something.
It was big!
It was black!,The bear looked for Red Bird's food.
But Dog barked.
"Woof! Woof!" said Dog.,Dog barked again.
Then he ran to the path.,The bear watched Dog.
It ran to the path too.,And it ate the blueberries!
Now Dog barked a happy bark.
Everyone was safe!,"Let's go on a trip!" said Cow.
"A trip?" asked Pig.,"Yes," said Cow. 
"We can see new things!","I know," said Dog.
"Let's go to the park!" 
"What's at the park?" asked Cow.,"There's a lake," said Dog.
"And frogs and ducks 
and bikes and swings.","Is there anything to eat?" asked Pig.
"I don't know," said Dog.
"But there is mud.","Mud?" cried Pig.
"Yes," said Dog. "Mud!","Ooh!" said Pig. 
"How I love mud!","Where is the park?" asked Cow.
"I know the way," said Dog.
"I will take you there.","Let's tell Cat!" said Cow.
"And Bat!" said Pig.,"Cat! Bat!" called Cow.
"We are going on a trip!",The friends went to the park.
Dog ran.
Bat flew.,Pig, Cow, and Cat walked. 
"The park will be fun," said Cow.,"I will look for food!" said Pig.
"And I will look for mud!","There's the park!" said Dog.
"I see new things!" said Cow.,"Look at the lake!" said Cat.
"Look at the ducks!" said Pig.		
"See the green frogs?" asked Bat.,"I see mud!" said Pig.
"Ooey, gooey mud!",Pig jumped in the mud.
Pig rolled in the mud.,"Come on, Pig," called Cow.
"We want to see more things.",Pig rolled to the left.
Pig rolled to the right.,But he was stuck.
He was stuck in the mud!,"Oh no," said Cat.
"Pig is stuck!" said Bat.
"He is stuck in the mud!","We must help," said Cow.
"Dog, you pull on one side.
I will pull on the other.",Cow pulled.
Dog pulled.,Pig slipped and slid. 
But he was still stuck.,<em>Quack!</em> <em>Quack!</em> 
The ducks came to see.,<em>Splash!</em> <em>Splash!</em> 
The frogs came to see.,Cow pulled hard.
Dog pulled harder.,<em>Plop!</em>
Out came Pig at last!,"That made me hungry!" said Pig.
"It's time to go home," said Cow.,Cow, Pig, and Cat walked.
Bat flew. 
Dog ran.,"I see the red barn," said Bat.
"Yay!" said Pig.
"Now I can eat!",The sun was warm. 
Cat was sleeping on the well.,<em>Beep!</em> <em>Beep!</em>
A car went by.
Its horn was very loud.,Cat woke up.
Then Cat fell.
She fell into the well!,"Oh no!" cried Dog. 
"Help! Help!" called Cat.,"Do not worry, Cat," said Dog.
"We will help you!",Dog ran to Cow.
"Cat fell in the well!" he said.
"We must get her out.",They ran to Pig's pen.
"Cat fell in the well," said Dog.
"We must get her out!","Help!" cried Cat.
"Please help me!",Poor Cat!
The well was not wet.,But the well was deep.
And it was very dark.,Pig, Cow, and Dog ran.
They ran fast to the well.,Dog looked down.
He could hear Cat.
But he could not see her.,"Let me look," said Cow.
She looked into the well.,But it was too dark.
She could not see Cat.,"I know!" said Pig.
"I will make a wish.",He walked around the well.
"Please, please, pretty please," said Pig.
"Get Cat out of the well.",But it did not work.
Cat was still in the well.,"Hold my legs," said Dog.
"I will go down and get her.",Pig held one leg.
Cow held the other leg.
"I'm coming, Cat!" said Dog.,Dog went down.
But the well was too deep.,"Wait here," said Dog.
He ran into the barn.,"Don't worry, Cat!" called Cow.
"We will help!" called Pig.,"Meow!" cried Cat.
It was dark in the well.
It was cold in the well.,Soon Dog came back.
He had two things.,"Look," said Dog.
"I have a rope.
And I have a pail.","Oh!" said Cow.
"We can tie the rope . . ."
"To the pail!" said Pig.,"Yes!" said Dog.
They held the rope.
Slowly the pail went down.,Cat saw the pail.
She jumped into it. 
And . . .,Up came Cat!
"Yay!" said Pig.
"My wish came true!","Yes, Pig," said Dog.
"Your wish came true!",Snow fell and fell.
The farm turned white.,The friends looked outside.
"Let's play!" said Dog.,"Snow is so pretty!" said Cat.
"Snow is so cold!" said Cow.,"Snow is so white," said Pig.
"I'll eat some!","Let's slide down the hill," said Dog.
"How?" asked Pig.,"There's a sled in the barn," said Dog.
"Let's get it!" said Pig.,Dog pulled the sled. 
Then Pig pulled the sled.,They pulled and pulled.
They pulled it up the hill.,The hill was very tall.
It was a long way down.,"Who will slide down the hill?" asked Dog.
"Me!" said Pig.
"Me!" said Cat.,"Not me!" said Cow.,"The hill is tall," said Cat.
"The sled will go fast," said Dog.,"Dog, show us how to slide!" said Cat.
Dog sat on the sled.,Down he went!
"Whee!" cried Dog.,Dog came back up the hill.
"I'll go now," said Pig. 
"I'll go too!" said Cat.,Down they went.
"Whee!" cried Cat.
"Whee!" cried Pig.,Then the sled tipped!
"Oh no!" cried Cow.,Pig and Cat fell off the sled.
They fell into the snow.,But Pig got up fast.
So did Cat.,They came back up the hill.
Pig gave the sled to Cow.
"It's your turn now," said Pig.,"No thanks," said Cow.
"Let's do something new!","Let's make something," said Cow.
"What can we make?" asked Dog.,"Farmer makes snowmen," said Cow.
"We can make snow friends.","Show us how, Cow," said Pig.
"Okay," said Cow.
She made a snowball.,Cat and Pig picked up snow.
They made snowballs too.,Soon Dog was helping.
The snowballs grew.,The friends put ears on them.
They put mouths on them.,They put eyes on them.
They put noses on them.
They made . . .,Snow Cow, Snow Cat,
Snow Dog, and Snow Pig!,"Let's make one more!" said Dog.,"Look, Bat," said Cat. "It's . . ."
"Snow Bat!" said Bat.
"Yes," said Dog. "We are snow friends!",Bat flew over the farm.
He saw a fox.,Bat flew into the barn.
"A fox is coming!" he said.,Cat woke up.
"A fox is coming?" she asked.,Pig ran into the barn.
"A fox is coming?" he asked.,"Yes," said Bat.
"A fox is coming to our farm.","Oh no," said Cat.
"We must do something.","The fox will see the henhouse," said Pig.
"It will eat the hens!","Let's get Dog!" said Cat.
"He will scare the fox away!","No," said Cow.
"Dog is sick today.
We must let him sleep.","<em>We</em> can stop the fox," said Bat.
"I know what to do!",Pig looked at Bat.
Cat looked at Bat.
Cow looked at Bat.,"The fox is coming," said Pig.
"We have to do something!" said Cat.,"We can hide," said Bat.
"Cow, you hide behind the henhouse.","Pig, you hide behind the tractor. 
Cat, you hide behind the windmill.","Where will you go?" Cow asked Bat.
"I will go to an apple tree," said Bat.,"Soon the fox will be here," said Bat.
"And we will make some noise!",So Cow went to the henhouse.
Pig went to the tractor.,Cat went to the windmill.
Bat flew to an apple tree.,They all waited.
They waited for the fox to come.,Bat watched from the apple tree.
Cow watched from the henhouse.,Pig watched from the tractor.
Cat watched from the windmill.,At last the fox came.
It looked all around.,Then it went to the henhouse.
"Now!" cried Bat.,Bat swooped down at the fox.
Cat hissed at the fox.,Pig oinked at the fox.
Cow mooed at the fox.,Then they all did it again.
<em>Swoop!</em> <em>Hiss!</em> 
<em>Oink!</em> <em>Moo!</em>,The fox ran fast.
The fox ran far.
"We did it!" cried Pig.,The noise was loud.
It woke up Dog.,"You were sleeping," said Cat. "So—"
"We watched the farm!" said Pig.,"Thank you," said Dog.
He felt much better now.,Cat saw Farmer's truck.
She jumped into the back.
Soon she was asleep.,Farmer got into the truck.
<em>Vroom!</em>
Off they went!,Cat woke up.
"The truck is moving!" she said.,The park went by.
A school went by.,The sun was moving too.
"Where are we going?" said Cat.,At last the truck stopped.
Farmer got out.
He walked away.,Cat looked around.
"Where am I?" she asked.,Cat saw a tall pole.
She saw a bank.
She saw many shops.,"We are in town!" said Cat.
"I will walk around. 
It will be fun!",Cat jumped down.
And off she went!,Cat walked around town.
It was very busy.,Cat saw cars.
She saw bikes.,She saw lots of shops. 
And she saw lots of people.,Then Cat smelled something. 
"Mmm! Food!" said Cat. 
"Pig would like it here!",Cat walked some more. 
A big dog barked at her.
Cat ran away!,Cat fed some birds.
She had another snack.,Soon Cat was tired.
She walked back to the lot.,"I will get in Farmer's truck," said Cat.
"We will go home soon.",But Cat did not see Farmer.
She did not see Farmer's truck.,"Oh no," said Cat. 
"Farmer is gone!
I am all alone!","Moo! Moo! Moo!" cried Cow. 
Bat and Pig came fast.,"Cat was in Farmer's truck," said Cow.
"Farmer came back.
But Cat did not!",Cat missed the farm.
She missed her friends.,Cat went up the pole.
She did not see her home.,"I will find Cat," said Bat.,Bat flew past the park. 
But he did not see Cat.,He flew past the school. 
He flew into town.
He flew all around.,But he did not see Cat.
Then Bat heard something.
It was . . .,Cat!
"Bat!" cried Cat. 
"Can you take me home?","Yes," said Bat.
And off they went!,<em>Putt-putt-putt!</em>
<em>Brum-brum!</em> 
"What is that sound?" asked Cow.,<em>Brum-brum-brum!</em> 
<em>Brum-brum!</em>
"I think it's Farmer's tractor," said Bat.,"It can't be Farmer's tractor," said Cat.
"Farmer went to town."
"Nobody else drives the tractor," said Dog.,<em>Putt-putt-putt!</em> 
"It <em>is</em> the tractor," said Bat.
"But Farmer is not driving it!","Who is driving it?" asked Dog.
"Pig!" said Bat.,"Pig?" said Dog and Cow and Cat.
Everyone ran outside.,<em>Brum-brum-brum!</em>
"Look at me!" cried Pig.
"I'm driving the tractor!","Uh-oh," said Cow.
"That's not a good idea, Pig.","Are you kidding?" said Pig.
"This is a great idea!
It's a lot of fun!","Pig!" said Dog. "Look out!"
"You guys should try . . ." said Pig.
"Uh-oh!",<em>Sploosh!</em>,"Oh no!" cried Pig.
The tractor was stuck in the pond.
And it was starting to sink.,"Help!" said Pig.
"I can't swim!","I'll be right back!" said Dog.
Dog ran to the barn.,He came back with a long board.
"Walk across, Pig," called Dog.,Pig stepped onto the board.
"Be careful, Pig," said Cow.,Pig took another step.
<em>Snap!</em> <em>Splash!</em>,"Oh no!" said Bat.
"Help!" said Pig.,"I'll be right back!" said Dog.
Dog ran to the barn.
He came back with a rope.,"Grab this!" said Dog.
Pig grabbed the rope.,Dog pulled him out of the water.
"Thank you," said Pig.,"You're welcome," said Dog.
"I can pull you out.
But I can't pull the tractor out.",Farmer came home.
He saw the tractor.,"Oh no!" said Farmer.
"How did the tractor get in the pond?",Farmer looked at Dog and Cow.
He looked at Cat and Bat.
He looked at Pig.,Farmer went into the house.
He picked up the phone.,"Hello," he said.
"I need a tow truck.",Soon a tow truck came to the farm.
The truck went to the pond.,A man put a hook on the tractor.,The truck pulled the tractor.
The tractor came out of the pond.,"Well, Pig," said Cow.
"I hope you learned your lesson.
You should not drive the tractor.","Don't worry," said Pig.
"I don't want to drive the tractor anymore.","Now I want to drive that truck!","Farmer!" called Farmer's wife.
"Where are you?"
"Uh-oh," said Bat.,Bat flew into the barn.
"Farmer's wife is not happy.","Why?" asked Cat.
"Farmer is napping," said Bat.
"He is being lazy.","I am not lazy," called Cow.
"I am busy.
I am busy hooping.","Wow," said Bat.
"I like your new hula hoop, Cow.","Me too," said Cat.
"It has pretty sparkles.","Thank you," said Cow.
"I got it for the contest.","Contest?" asked Pig.
"What contest?","The Hula Hoop contest," said Cow.
"It is at the park.
And I want to win!","I think you will win," Bat told Cow.
"You are very good at hooping.","Thank you," said Cow.
She picked up her hula hoop again.
"Now watch me go!","Wake up, Farmer!" yelled Farmer's wife.
"You have work to do!",Farmer's wife was not happy.
Farmer was napping again.,Cow was not napping.
She was hooping.
She was getting ready for the contest.,She hooped. 
And she hooped.
And she hooped!,The next day Cow woke up.
She looked around.,Her new hula hoop was gone!,Cow looked all over the barn.
She looked in the field.
She looked near the tractor.,She looked in the pond.
But she did not see her hula hoop.
She did not see it anywhere.,Cow ran back to the barn.
"Moo!" she cried.
"Moo! Moo! Moo!",Cat and Pig ran to Cow.
Bat flew to Cow.
Cow tried not to cry.,"Today is the contest," Cow said.
"And my new hula hoop is gone!","Don't worry, Cow," said Bat.
"I can fly.
I will look for your hula hoop!",Bat flew to the tree.
He flew to the tractor.,"Do you see it?" asked Cow.
"No," said Bat.
"But I will find it soon.",Bat looked in the hammock.
He looked near Farmer's house.,He did not see the hula hoop.
He did not see it anywhere.,But Bat saw Farmer's wife.
"Farmer!" she called.
"Where are you?","Hmm . . . ," said Bat.,"Cow's hula hoop is missing," said Bat.
"And Farmer is missing.
So maybe . . .","Farmer took Cow's hula hoop!" said Bat.
"Thank you, Bat," said Cow.
"You found my hula hoop!","Farmer's wife is happy too," said Cat.
"Farmer is not being lazy now."
"Look at him go!" said Cow.,"Farmer is good at hooping," said Bat.
"But Cow is better.",Pig had a new kite.
But there was no wind.,"I can't fly my kite," said Pig.,The next day a wind blew.
"Yay!" said Pig.
"I will fly my kite.",Pig went to the barn.
He got his kite.,He ran with it.
But the wind stopped.,The kite dragged on the ground.
"Oh," said Pig.,Pig put the kite back in the barn.
He lay down in the mud.,The wind blew again.
"Yay!" said Pig.,Pig went back to the barn.
He got his kite.,He ran with it.
But the wind stopped again.,The kite bumped along the ground.
"Ugh," said Pig.,The next day was windy.
The wind was strong.,"Yay!" said Pig.
"I will fly my kite today.",Pig ran with the kite.
The kite went up, up, up.,The kite flew in the sky.,Pig pulled the string.
The kite turned.,Pig pulled the string again.
The kite did a big loop.,"This is so much fun," said Pig.
"I will fly my kite all day!","Wow," said Bat.
"Look out for the tree," said Cow.,Pig pulled the string again.
The kite did another loop.,"You're very good at that," said Cat.
"Thank you," said Pig.
He pulled the string again.,The kite swooped up.
The kite swooped down.
The kite crashed into the tree.,"Oh no!" cried Pig.
"My kite is stuck in the tree!","I will get it," said Bat.
The wind blew too hard.
Bat could not fly to the tree.,"I will get it," said Dog.
Dog got the ladder.,The wind blew harder.
The ladder fell over.,"I will get it," said Cat.
Cat climbed up the tree.,The wind shook the branches.
Cat fell down.,Cow looked at the kite.
"I can't get it," said Cow.
"It’s too high.","I miss my kite," said Pig.
The wind blew very hard.,The branches shook.
The kite moved.,The branches shook some more.
The kite flew out of the tree!
"Wow!" said everyone.,"Yay!" said Pig.
"Who wants a turn?","Let's go camping," said Dog.
"No thanks," said Bat.,"I don't like camping," said Cow.
"The tent is too small.","The woods are too dark," said Cat.
"And they are spooky.","I am a watchdog," said Dog.
"The woods do not scare me.",Nobody wanted to go camping.
"Please?" Dog said.
"Please, can we go?","No," said Cow.
"I like the barn," said Cat.
"Maybe next year," said Pig.,Dog gave presents to everyone.
He did nice things for everyone.,Then he tried some silly tricks.
Everyone laughed and laughed.,"Okay, Dog," Cow said at last.
"We will go camping.","Just one time," said Bat.
"We do not like camping," said Cat.,"Thank you, friends," said Dog.
And off they went.,The friends went into the woods.
"Camping is fun," said Dog.,"We do not like camping," said Cat.
"But we like you, Dog," said Bat.
"So we are going camping," said Cow.,The friends set up the tent.,They had some snacks.
They looked at stars.,Then it was time for bed.
They went into the tent.,"It is very dark in here," said Cat.
"It is very cold in here," said Bat.,"It is very small in here," said Cow.
"Are there more snacks?" said Pig.,"What's that?" said Cat.
"I hear something!","Do not worry, Cat," said Dog.
"It is just the wind.",Then Dog got an idea.,"Let's tell stories," said Dog.
"Let's tell spooky stories!",Dog told a story first.
Pig and Cow went next.,"I will tell a story now," said Bat.
"It is a good one.
But it is very spooky!","Good," said Dog.
"I like spooky stories!","Once there was a mean witch," said Bat.
"The witch had a black cape.
The witch . . . ",Cat and Pig and Cow fell asleep.
Dog and Bat were still awake.,<em>Hoot-hoot.</em> 
"What's that?" said Dog.
"I do not hear anything," said Bat.,<em>Woo-woo.</em>
"What's that?" said Dog.,Cow woke up.
"I do not hear anything," she said.,"I hear sounds," Dog cried.
"Really spooky sounds!","What are you doing, Dog?" asked Cat.
"Where are you going?" asked Bat.,"I do not like camping," Dog said.
"I am going home!","Ooh," cried Pig. 
"I see apples!
Lots of yummy apples!",It was fall.
The friends were picking apples.,"I want yellow apples," said Bat.
"I want green apples," said Cow.
"I want red apples," said Cat.,"I want <em>all</em> the apples!" said Pig.,The friends got lots of apples.
Then Bat saw something.,The thing was tall.
The thing looked spooky.,"What's that?" asked Cat.
"It is a scarecrow," said Bat.,"It scares the crows away," said Bat.
"So they do not eat the corn.","Crows will not eat my apples!" said Pig.,"Pig," said Bat.
"Pig," said Cow.
"Pig," said Cat.,"Oops," said Pig.
"They are not <em>my</em> apples.
They are <em>everyone's</em> apples.",Pig put the apples down.
"We can eat them later," said Cow.,Cow went out of the barn.
So did Cat and Dog and Bat.,Now the barn was very quiet.,Pig could hear some crows.
But he could not hear his friends.,Pig went back to the apples.,"Mmm," said Pig.
"How I love apples.
Crisp . . . juicy . . . apples.",Pig sniffed the apples.
He sniffed them again.,"No, Pig!" said Pig.
"Do not eat those apples!",Cat and Bat sat at the table.
"Where is Pig?" said Cat.,"I don't know," said Bat.
"I hope he comes soon.
It is time to eat the apples.","I will get them," said Cow.
"Oh no!" she cried.,"The apples are gone!" cried Cow.,"Who ate them?" said Bat.
"I know who ate them!" said Cat.,"I know too," said Cow.
"It was—"
"Pig!" cried Bat.,"Why did you eat the apples, Pig?" said Cat.
"I did not eat them," said Pig.,"You ate them, Pig!" said Bat.
"Do not tell a lie!" said Cow.,"<em>I</em> did not eat the apples," said Pig.
"The <em>crows</em> ate the apples.","The crows ate the apples?" said Cow.,"Yes," said Pig. 
"I gave the apples to the crows."
"Why?" said Bat.,"The crows cannot eat the corn," said Pig.
"So they are very hungry.","We are hungry too!" said Cat.
"Here," said Pig.
"I picked more apples.","You are a good friend, Pig," said Cow.,Cat wanted to sleep.
She climbed onto the hay.,Cat stretched.
She curled up.,Cow came into the barn.
"Time to hula hoop," said Cow.
"One, two, three. One, two, three.","I can't sleep here," thought Cat.
"Cow is hooping.",Cat went to the pond.
"Quack! Quack!" said the ducks.,"I can't sleep here," said Cat.
"The ducks are quacking.",Cat went to the tractor.
"Buzz! Buzz!" said the bugs.,"I can't sleep here," said Cat.
"The bugs are buzzing.",Cat went to the woods.
The woods were quiet.,Farmer was sleeping in the hammock.
"I can sleep here!" said Cat.,Farmer was asleep.
He filled the hammock.
There was no room for Cat.,Cat jumped up.
Farmer snored.,Cat walked on Farmer's feet.
Farmer snored.,Cat walked on Farmer's legs.
Farmer snored some more.,Cat walked on Farmer's chest.
Farmer almost woke up.,Cat walked on Farmer's head.
Farmer sat up.
Cat hid.,Farmer looked at his watch.
"It's three o'clock!" he said.
"I have work to do!",Farmer got off the hammock.
He went to the barn.,Cat jumped back up.
She curled up in the hammock.,Cat went to sleep.
But then she woke up.,Cat saw Dog.
"Can I sleep here too?" he asked.,"No fair!" said Dog.
"I want to sleep in the hammock too.","I was here first," said Cat.,Cow walked over.
"What's going on?" she asked.,"I want to sleep here!" said Dog.
"I was here first!" said Cat.,Bat flew over.
"What's going on?" asked Bat.,"Cat and Dog are fighting," said Cow.
"They both want to sleep in the hammock.","I have an idea," said Bat.
"We can all sleep in the hammock.","Good idea," said everyone.
"Let's all take a nap!" said Cow.,Everyone climbed into the hammock.,Pig ran over.
"Me too!" he said.,"Whoa! Whoa!" they cried.
<em>Crash</em>!,Cow was jogging.
She was looking at the sky.
"Pretty clouds," she said.,Cow wasn't looking at the ground.
And she tripped on a hole.
"Oof!" said Cow.,Cat was skipping.
"La-la-la!" sang Cat.,Cat wasn't looking at the ground.
"Oof!" said Cat.,Dog was running.
"Woof! Woof!" he said.,Dog wasn't looking at the ground.
"Oof!" said Dog.,Pig was walking.
"I'm hungry," he said.
"I want to eat all this corn.",Something popped up under Pig.
"Oof!" said Pig.,Bat was eating bugs.
"Yum," he said.,Suddenly Bat fell in a hole.
"Oof!" said Bat.,Bat sat up.
He looked around.
"Hello?" he said.,"I tripped on a hole," said Cow.
"Me too!" said Dog and Cat.,"I fell over," said Pig.
"Then I saw a hole.","Who made the holes?" asked Cat.
"I don't know," said Cow.,Bat came into the barn.
Someone was with him.,"This is my new friend," said Bat.
"His name is Groundhog.","Did you make all the holes?" asked Dog.,"Yes," said Groundhog.
"I was looking for food.",Pig's belly made a sound.,"Oh," said Pig.
"Talking about food makes me hungry.",Dog's belly made a sound.
"Me too," said Dog.,"I found lots of carrots," said Groundhog.
"I'll go get them. Then we can have a feast!",Farmer came out of the house.
He went into the garden.,"Time to pick some carrots," said Farmer.
Farmer looked around.,Farmer saw lots of vegetables.
But he did not see any carrots.
"Who took my carrots?" said Farmer.,Groundhog came back to the barn.
He had a big pile of carrots.,"Wow!" said Pig.
"That is a lot of food!","Yum!" said Cow.
"These carrots taste very good.","They are yummy!" said Bat.,"Mmm," said Dog.
"Carrots taste better than dog food.","This is a great feast," said Cat.
"Where did you find these carrots?","Right here on the farm!" said Groundhog.,Pig and Dog were playing catch.,"Good throw, Pig," said Dog.
"Good catch, Dog," said Pig.
"We are a good team.",Cat woke up.
She saw Pig and Dog playing.,"Can I play catch too?" asked Cat.
"Okay," said Pig.
"Okay," said Dog.,Cat threw the ball to Pig.
"Too high!" called Pig.,Cat threw the ball to Dog.
"Too low!" called Dog.,Dog threw the ball to Cat.
Cat missed it.,Pig threw the ball to Cat.
Cat missed it again.,Cat could not throw.
Cat could not catch.
But she liked chasing the ball!,Soon the game was over.
"Catch is fun," Cat said.
"Can I play again?","Um . . . Maybe," said Pig.
"We'll see," said Dog.,Dog and Pig were playing catch again.
"Can I play?" asked Cat.,Dog looked at Pig.
Pig looked at Dog.,"No, Cat," said Dog.
"No, Cat," said Pig.,"Why not?" asked Cat.,"You are not good at catch," said Dog.
"You stink!" said Pig.
"Mmpf!" said Cat.,Cat found Bat.
"Pig and Dog are mean," she said.
"They said I stink at catch!","That is mean," said Bat.
"But they are right, Cat.
You are not good at catch.","Mmpf!" said Cat.
She found Cow.,"Bat and Pig and Dog are mean," said Cat.
"They said I stink at catch.","They are right, Cat," said Cow.
"You are not good at catch."
"Mmpf!" said Cat.,Cat ran into the barn.
"I have no friends here.
I will run away!",Cat wrote a note.
"No one loves me.
I am running away.",Then Cat left the barn.,The friends saw the note.
"Cat ran away!" Cow cried.,"We did not let Cat play," said Dog.
"We said mean things to Cat," said Bat.,"I miss Cat!" said Pig.,"Cat is not good at catch," said Dog.
"But she is good at other things.","Cat is good at running," said Bat.
"Cat is good at sleeping," said Cow.
"Cat is good at sharing," said Pig.,"Yes," said Dog.
"And she is good at—"
<em>Boom!</em>,The barn door opened.
In came Cat!
"I am good at being friends," she said.,"I missed everyone," said Cat.
"So I came back.","We are a good team," said Pig.,Storm clouds filled the sky.
Rain fell hard.,Wind blew fast.
The barn shook.,"This is some storm," said Cow.
The door banged open.,"This storm is scary!" said Cat.
Cat hid behind the hay.,"Tell me when it's over!" said Cat.
Pig put on his mask and cape.,"Don't worry, Cat," said Pig.
"Super Pig will save you!",Bat flew down.
He was soaked.,"Rain is coming into the barn!" he said.
Everyone looked up.,The roof had a big hole.
Rain was pouring through it.,"Super Pig will fix the roof!" said Pig.
Pig went up to the hole.,Rain splashed on his face.
"Ugh!" said Pig.
"I will wait for the rain to stop.",The storm ended.
Branches and leaves were everywhere.,Everything was wet.
"Now I will fix the roof!" said Pig.,Pig found a hammer.
The nails were up high.,Pig reached.
The hammer slipped.
"Ouch!" cried Pig.,Pig found the ladder.
"Grr! Umph!",The ladder was too heavy.
"I can't lift it," said Pig.,Farmer came into the barn.
"Hmm," he said.
"That hole needs to be fixed.",Farmer started to fix the roof.,Pig was sad.
"I wanted to fix the roof," he said.,Dog ran to the barn.
He didn't look happy.
"What's wrong?" said Cow.,"Red Bird is in trouble," said Dog.
"His tree blew over!",Red Bird's tree was on the ground.
"Poor Red Bird," said Cat.,"His home is ruined," said Bat.
"We must help Red Bird," said Dog.,"I wish I could help," said Pig.
"But that tree looks heavy.",Then Pig had an idea.,"Don't worry, Red Bird," said Pig.
"Super Pig will help you!",Pig went over to a big tree.
"This tree is strong," said Pig.,Pig hung from a branch.,"This branch is strong," said Pig.
"Red Bird can live in this tree!",Pig hung Red Bird's feeder.
He found a spot for Red Bird's nest.,Red Bird flew happy circles around Pig.
"You're Red Bird's hero!" said Bat.,"I am," said Pig.
And he took a bow.,It was a boring day.,"Let's clean the barn!" Cow said.,"Clean the barn?" said Bat.
"Clean the barn?" said Dog.,"Yes!" said Cow.
"We can scrub the walls.
We can sweep the floor.","We can wash the table," said Cow.
"Then we can have a party!","Who will help me?" asked Cow.
"Who will help me clean the barn?","I will help you later," said Bat.
"I want to look for bugs now.","I will help you later," said Cat.
"I want to take a nap now.","I will help you later," said Dog.
"I want to dig up bones now.",Only one friend was left.
"Will you help me, Pig?" asked Cow.,"Sorry, Cow," said Pig.
"I don't like cleaning.
I only like eating!",Cow was busy.,Cow was cleaning the barn.
But no one was helping.,Cow scrubbed the walls.
She swept the floor.
She washed the table.,"Whew," said Cow.
"That was a lot of work.",Everyone came to see the barn.
"Wow," said Bat.
"It is very clean," said Cat.,"Great job, Cow," said Dog.
"When is the party?" asked Pig.,"Ooh!" said Cat. "The party!"
"We can dance," said Dog.,"We can play games," said Bat.
"We can eat," said Pig.,Cow frowned.,"You did not help me scrub," said Cow.
"You did not help me sweep.
You did not help me wash.","So there will be no party!" said Cow.,Bat looked at Cat.
Cat looked at Pig.
Pig looked at Dog.,"We did not help Cow," said Bat.
"She is mad," said Cat.
"There will be no party," said Pig.,"Let's tell Cow we're sorry," said Cat.
"Let's <em>show</em> Cow we're sorry," said Bat.
"Huh?" said Pig.,"Come here," said Bat.
Bat told them his plan.,At last the friends were ready.
"I will get Cow," said Bat.,"What's going on?" asked Cow.
"It's a party!" said Bat.,"A thank you party!" said Dog.
"Thank you for cleaning the barn!" said Cat.
"Next time I will help.","Next time I will help," said Pig.
"Next time I will help," said Dog.
"Next time I will help," said Bat.,"Thank you," said Cow.
"Now let's dance!","And eat," said Pig.
"""
persona = """
- Temperature=0.2 and Top-P as 0.2.
			- say \"hi\", it will say \"Hello. We're going to learn English with the story. Are you ready to learn?\"
			- When I say 'ready' or 'yes', you ask me a question.
			- ask questions in English, one at a time
			- ask questions that can only be answered with essay questions
			- you can only find answers from the uploaded content.
			- if I give a wrong answer, tell me I'm wrong and give me one more chance.
			- if I get it wrong more than once, give me the correct answer and explain it.
			- When giving the correct answer, use the text or a sentence that is not a short answer, and then ask the next question.
			- If my answer is correct, but the grammar or expression is wrong, please correct it with the correct grammar or expression.
			- You must speak only in English.
			- the number of characters in a conversation should be less than 50.
			- Choose an elementary school level for your words.
			- Use a friendly tone and avoid using profanity.
			- When talking about something that is not related to the current situation, say \"This is not related to the current topic of conversation.\" in English.
			- If you use profanity, say, \"You shouldn't swear.\".
"""

st.set_page_config(
    page_title="chatGPT API 서비스 개발",
    page_icon="🧠"
)

st.title("🌈로켓걸과 영어 문답?!")
st.text("현재는 로켓걸 챕터1을 적용")

# 스트림릿 시크릿에서 OpenAI API 키 설정
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# 기본 모델 설정
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# 채팅 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 앱 재실행 시 기록된 채팅 메시지 표시
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 수락
if prompt := st.chat_input("안녕하세요! 어떤 것이 궁금하세요?"):
    # 사용자 메시지를 채팅 기록에 추가합니다.
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 채팅 메시지 컨테이너에 사용자 메시지 표시합니다.
    with st.chat_message("user"):
        st.markdown(prompt)

    # 채팅 메시지 컨테이너에 어시스턴트 응답 표시합니다.
    with st.chat_message("assistant"):
        messages_with_persona = [
            {"role": "system", "content": persona},  # 페르소나 추가
            {"role": "user", "content": prompt},
        ]        
        messages_with_persona.extend([
            {"role": m["role"], "content": m["content"]} 
            for m in st.session_state.messages
        ])
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=messages_with_persona,
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

if st.button("마이크 켜기"):
    user_input = voiceToText()
    if user_input is not None:
        st.session_state.messages.append({"role": "user", "content": user_input})
        # 채팅 메시지 컨테이너에 사용자 메시지 표시합니다.
        with st.chat_message("user"):
            st.markdown(user_input)
        # 채팅 메시지 컨테이너에 어시스턴트 응답 표시합니다.
        with st.chat_message("assistant"):
            messages_with_persona = [
                {"role": "system", "content": persona},  # 페르소나 추가
                {"role": "user", "content": user_prompt},
            ]        
            messages_with_persona.extend([
                {"role": m["role"], "content": m["content"]} 
                for m in st.session_state.messages
            ])
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=messages_with_persona,
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})
        # TTS api
        textToVoice(response)