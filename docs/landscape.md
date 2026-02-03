Bardzo chciałbym zrozumieć i przewidzieć rynek w kontekście AI i możlwiosci wdrożenia w firmach, co moze być selling point, co jest potrzebne biznesowi, co jest potrzebne deweloperom, czego jeszcze (jakich okacji) nie wykryto w kontekście mżliwości AI, teraz zajmuję się pisaniem procesów walidacyjnych tego co wykonało AI, ale albo tak jal w BMAD jest to proces tworzenia PRD, epic, archtecture, story, sprints, dewelopment, oraz tworzenia testów, dewelopowania tego co zostało do wykoania, ale wszystko jest nie do końca bo takie jakbbym chcał, 

z jednej strony mamy takie coś jak proces w @C:\Users\lukasz.krysik\Desktop\deep-verify\deep-verify\_bmad\bmm\workflows i są to opisy co zrobić, jak zrobić, co po kolei ale jest to w markdown, małą analizę mam w @C:\Users\lukasz.krysik\Desktop\deep-verify\deep-verify\docs\bmad\bmm.md, 
nie da się tego kontrolować niestety w jakiś determistyczny sposób, czyli na przykład przy użyciu python albo innego kodu, każda zmiana w bmad\bmm będzie wymagała głębokich zmian w kodzie python, być może przemyślany sposób na tworzenie kontraktu miedzy bmad\bmm powinna istnieć, tak żeby każdy krok / workflwo / agent miał swój manifest / kontrakt i najlepiej by byl częscią markdown gdzie opisany jest step / workflow / agent w taki sposób by python mógł to odczytać ale żeby nie ingerować w same procesy bmad , trzeba by też mieć jakieś relacje między tymi zadaniami bo obecnie na przykład workflow ma steps które są w jakiejś kolejności, produkują też określone treści albo oczekują konkretnych treści, dodatkowo steps czy workflow wymagają istnienia lub wykonania innych kroków, 
jeszcze trudniej się robi gdy mamy epic / architecture / prd / story są efektem pracy bmad / bmm co jest w samo w sobie zagadnieniem, ale jeżeli można by to też zamienić coś w wewnętrznego take żeby poza treścią epic / architecture / prd / story miały swoje kontrakty by można je kontrolowac przez python wtedy kod python staje się bardziej generyczny bo odczytuje kontrkty i może je po pierwsze łatwo prezentować, po drugie modyfikować, bo jak powstaną epici to można zmieniać kolejność 
do tego można zejśc głębiej bo w dokumencie prd powstają wymagania funkcjonalne i niegunkcjonalne , jeżeli zostanie zachowana jakaś struktura i te dokumenty będa generowane przez LLM w sposób zapewniajacy zgodnośc z jakims wzorem to python czy jakikolwiek kod będzie mógł to konrolować, wskazywać zalezności , na przykład miedzy epic / story a wymaganiami funkcjonalnymi i nie funkcjonalny, albo architektura też jest czymś co można jakoś rozwiazać , do tego można by wprowadzić w kodzue python lub innym język walidator który sprawdza czy efekt pracy - to co wyprodukuje LLM w jakimś kroku jest zgodne z standardową strukturą, 

jeszcze właśnie nie znam ograniczeń i trochę się obawiam że nie wszystko przewidzialem, trzeba by to uważnie rozpatrzeć, jak zapwenić elastycznosć jaką zapewnia LLM by nie utracić tego zę można dopisać coś i nagle proces może robić coś innego, a czymś deterministycznym jak python który lepiej pozwala wizualizować i pokazywać użytkownikowi oraz egzekwować kolejnosc wykonania, co ważne jest tęż koniecznośc zapisywania 


jezęli mam mam opisany proces i kroki postępowania dla LLM w postaci markdown, to jest trudno wizualizować, to trudno jest też to co stworzy LLM szybko modyfikować, na przykłąd zmienić kolejność jeżeli stworzy          projekt epic, czy sprint, do tego jakby chciał na przykłąd zrobić proces który będzie wykonywany przez python to trudno jest wskazać jakie są kroki do wykonania bo mamy tylko pliki markdown, a jeszcze gorzej jest    
   jak cos sie zmieni w plikach markdown na przykłąd kolejnosć wykonania, trzeb wtedy przepisywać python zeby to odzwierciedlić, ale z drugiej strony nie chce utracić dynamiczności procesu, bo obecnie do wykonania      
  proces zapisanego w markdown wystarczy LLM (gemini cli czy claude cli) i mogło by tak zostać, ale w przypadku gdybym chcial dodać możlwiosc wizuwalizowania, sprwadzania co zostalo wykoanne, gdie jesteśmy zmiany       
  kolejnosci to jakaś warstw a pośredni jest potrzebna , lekka warstwa która jest obecna na miejscu w plikach markdwon bo nie może istnieć jako oddzielna struktura bo będzie też trudna do dostosowania do zmian w        
  markdown, to musi być częśc mardkown ta warstwa pośrednia zarówno odczytywalna i używana przez LLM jak i przez python co oznacza że zarówno LLM dobrze wie co trzeba zrobic z tym i jest to częsć procesu jak i          
  python potrafi to odczytać i interpretowac, i jeżeli ustandaryzujemy ten kontrakt to będzie on mówił co , gdize, dlaczego, kiedy, co nastepne itd itd                                                                    
 

 Ale generalnie chciałbym odkryc co mogę zmienić, gdzie cos stworzyć 

 Ale dla mnie problemem jest też to żeby w podstawowej wersji sam claude cli czy gemini cli bylo w stanie kontrolować i wykonywać proces
 ale możliwe było dodanie python lub innego języka ktory przez kontrakty będzie mógł ten proces wykonywąć, pokazywać, może nawet zmieniać (na przyklad przez listowanie i dostep do treści kroków albo kolejności)


 Wyniki pracy LLM są trudne do szybkiej modyfikacji przez kod  ale też kroki w markdown są trudne do śledzenia przez kod python, na przykłąd jakbym chciał stworzyć jakie są zależności miedzy krokami to nie da sie      
  tego zrobić bo zapis jest luźny w markdown, ale z drugiej strony to zaleta bo można proces zmienic tylko pisząc jakies dodatkowe luźne informacje, jak sobie z tym proadzić, bo na przykład tekst w markdown może na     
  przykład mówić wykonaj to i to, otwórz tamten plik oraz wykonaj jeszcze ten proces - ciężko to jakoś mapować na coś standardowego tak żeby nie stracić elastycznosc i markdown ale mieć z poziomu python wglad w to co   
  robi dany krok i jakie są zależnosci itd, jak pogodzić elastyczność markdown i LLM z możliwością kontaktu z kodem deterministycznym - to jest głównny cel    


  Główny cel to godzić złożone procesy opisane luźnie w markdown które LLM przeczyta z kodem python ktory może przeczytać za pomocą jakiegoś kodu i mapowć ten opis na kroki postepowania, a nawet wykonywac małe kroki przez wskazanie LLM który wykona dany krok lub część kroku, 

  Jak nie stracić luźnego elastycznego pisania po ludzku z możliwością raportowania, wykonywania podzadań, 
  a co wiecej jak zrobić tak że cały czas LLM będzie mógł wykonywac te procesy tak jak do tej pory gdzie jest opisane, idź otwórz ten plik ,przeczytaj a potem przygotuj analizę i LLM to wykona, natomiast python nie jest w stanie określić co to robi i kolejności , 

  jeżeli zaczniemy narzucać jakąś strukturę w markdown to tylko utrudni , ale z drugiej strony inaczej python nie ogarnie