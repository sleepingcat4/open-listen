I have reverse-engineered one of the most popular application, I have been bombarded lately across different platform through ads. AKA listening[dot]com. https://www.listening.io/

I was really bothered so I read their website and was wowed, how they were taking advantage of people by offering something so minimal. 

Listening[dot]com/io provides users to upload research papers and converts into audible voice so user can listen like podcast rather reading. Sounds scary! If you're not into Deep Learning. 

I wore my tin-foil hat and started reading through papers, luckily! I didn't needed to resort to old OCR libraries, Meta was kind to Open Source "Nougat" a leading solution in OCR. 

I applied Nougat combined with Google Text-to-Audio library (Public API) and made the same product like Listening[dot]com/io in practically spending nothing. 

### What I learnt?

Startups tend to scam people by over-hyping what they can provide. I totally believe converting papers to audio can be helpful for students but if you're trying to make your business around it then someone like me will close your shop in matters of days if not hours. 

### Why I did it?

I was motivated by their annoying ads. Please don't spam until you've a solid product : ) 

Oh, by the way, I was looking to try Nougat library lately that's another reason. 

### Current limitations

-  It converts latex structures into audio equally as I didn't add any pre-processing function yet to remove them after applying OCR 
- Google TTS (Public API) is limited to 100 req/hour. Limiting anyone to convert large scale audio
- It's not a library yet so? You need to use git to install and use it

### Upcoming Upgrades

- [ ] Adding pre-processing
- [ ] Writing logic to avoid Google's limitation
- [ ] Making it a library

Contribution
Please, contribute and if you have other ideas, feel free to implement. That's how, Open Source works. And don't fall for scam startups by paying them your hard-earned cash. Stay safe! ^^
