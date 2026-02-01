Mam pomysł na kilka procesów, 
istniejący proces deep-verify który jest w C:\Users\lukasz.krysik\Desktop\deep-verify\deep-verify\src\core\deep-verify\workflow.md (to jest entry point)
instniejący proces deep-explore ktory jest w C:\Users\lukasz.krysik\Desktop\deep-verify\deep-verify\src\core\deep-explore\workflow.md (to jest entry point)

ale chce stworzyć jeszcze deep-challenge do rozmowy z użytkownikiem i wyciągania wiadomosci
chce stworzyć deep-feasibility do oceny możliwości wykonania czegoś (głównie na podstawie deep challenge oraz deep explore)
oraz stworzyc deep-requirements, deep-risk, deep-synthesis, deep-plan

jest też projekt BMAD ktory można znaleźć w C:\Users\lukasz.krysik\Desktop\deep-verify\deep-verify\_bmad\bmm
służy do tworzenie wymagań, PRD, wymagań funkcjonalnych i niefunkcjonalnych, tworzenie epic, story, sprintów, architektury i inncyh rzeczy, jest to scenariusz który dobrze się sprawdza jak na razie do tego, 

tylko że ja chcę mieć też deterministyczne kroki, żeby bylo można je dynamicznie dopasowywac, dodawac jako listę, że nie tylko staly scenariusz, ale żeby to skłądało się z listy kroków, może jakiś zależności, i jezeli LLM na podstawie jakiś działań znajdzie że coś trzeba jeszcze przeanalizować rozszerzyć to żeby dodawać do listy kroków , tylko mam obawy że jedno z drugim się nie łączy, bo z jednej strony mam moje procesy deep verify, explore i przyszłosci , i chciałbym w jakiś sposób realizować i rozwijać jakiś projekt, powiedzmy dotyczący kodu, i moje wymagania się zmieniają, są takie które są ważne na początku, później są już mniej istotnte, to się zmienia, PRD się zmienia, potrzeby się zmieniają więc i proces musi się zmieniać, musi czytać inne rzeczy, bo co innego stworzyć projekt od podstaw, a co innego dalej go rozwijać, inne rzeczy staja sie ważne, na przyklad rozumienie co jest w kodzie bo kod staje sie duży i każda zmiana wymaga głębszej analizy, rozpoznania, zaplanowania, niż w przypadku gdy nie mamy nic i tylko dodajemy, 
dlatego potrzewuje dynamicznej liczby krokow która będzie dodawana wraz z wymaganiami ktore będą spływać, które będą kształtować wymagania a pewne wymagania deaktualizować.

też jakoś zainteresował mnie sposób zapisu działań, pewna notacja w przypadku użycia moich procesów deep 

bo na przykład mamy [pomysł] i jest to mój [artefakt_1] i jeżeli zastosuję na [artefakt_1] moje procesy deep explore i deep challenge to otrzymam [artefakt_2]
więc mogę to zapisać jako [artefakt_2] = deep-challange(deep-explore([artefakt_1])) lub krócej [artefakt_1] = dq(de([artefakt_1])) ale można też zapisac jako 
[artefakt_2] = de([int_artefakt_2_de_1]~de([artefakt_1])) czyli że [artefakt_2] jest wynikiem deep explore na obiekcie [artefakt_1] i wynik zapisało jako [int_artefakt_2_de_1] (jako pośredni element) a na tym wyniku [int_artefakt_2_de_1]  wykonano nastepnie deep-challange dzieki temu można śledzić jakie kroki i jakie wyniki i gdzie  
i jeżeli mój [pomysł] będzie zapisany jako mój_pomysł.md to łatwo kontrolować co i jak i gdzie 

Nastomiast mam obawy że nie łączy sie taki zapis z BMAD i jego BMM 

ALe ten zapis pozwala na określenie kroków jakie trzeba wykonać, na czymś takim można stworyzć plan rzeczy do realizacji 
bo na przykłąd [artefakt_14] = deep-synthesis([artefakt_5], [artefakt_6], [artefakt_7]) to wtedy wiemy że syntez informacji pochodziła z [artefakt_5], [artefakt_6], [artefakt_7]
i każda ta metod powinna mieć opisany w jaki sposób jest wykonywania 
że deep-verify() przyjmuje listę argumentów deep-verify([],[],[]) te argumenty mogą mieć różne znaczenie i różne weryfikacje, bo może być deep-verify([a]<-[b]) zweryfikuj czy [a] zgadza sie z [b] - czyli czy dokładnie to co jest w b ma przełożenie na a (ale już nie odwrotnie), albo deep-verify([a]<->[b]) czy jedno i drugie ma to samo, czyli jeżeli coś jest w a to i musi miec odpowiednik w b, albo przez negację deep-verify([a]<-~[b]) że to co jest w b nie ma przełożenia na a, że ten zapis jest odwracalny i matematyczny 
można by też opisywac zakres tego


i teraz można by zapisać cały proces jako deep-verify([a]<-[b]:{spójność, logika, klarowne}), żeby sprawdzić czy dokładnie to rzeczy z b zostały przeniesione do a w sposób spójy, logiczny i klarowny itd 

lista zadań / kroków
[artefakt_1] = [pomysł]
[artefakt_2] = de([artefakt_1]:{spójne})
[artefakt_3] = dq([artefakt_1])
[artefakt_4] = deep-risk([artefakt_3]:{sukces, technologie})  - jakie są ryzyka dla sukcesu (w obszarze sukcesu) oraz jakie są ryzyka technologicnze
[artefakt_5] = deep-synthesis([artefakt_3] <- [artefakt_4]) wykonaj syntezę rzeczy z [artefakt_4] do [artefakt_3] czyli uzupełnij wiedzę o to co jest w [artefakt_4]
[artefakt_6] = deep-compliance([artefakt_5]:{HIPAA}) - czy [artefakt_5] spełnia wymagania HIPAA ochronę prywatności i bezpieczeństwa wrażliwych informacji zdrowotnych

cały proces mógłby być zapisem takim. tylko obawiam się że dla LLM moze być to trudne, wiec muszą być jasne zasady 
artefakt to wynik, jest to forma kontraktu jaki mamy zawarty z procesami deep które tworzą artefakty i przyjmują artefakty, 
teraz jeżeli zapiszemy to jako listę działań to taki moduł BMM z BMAD też może da się tak zapisać, ale konieczna jest forma kontroli, co zostało wykonane, gdzie zapisane, jakiś sposób odczytywania gdzie jesteśmy, co można wykonać następne a czego jeszcze nie, trzeba też móc zapisywać tą listę (ten plan działań), dlatego LLM musi mieć zdefiniowany jasny i klarowny standard, jak czytać, jak zapisywac, jak sledzić, jak raportować wykonanie, jak szybko odczytywać informacje o danym kroku co w nim powstalo i gdzie, nawet forma dashboardu powinna być dostepna, czyli raportowanie postępów.

Teraz jak możemy podjeść do BMM, gdzie proces tworzy PRD , tworzy wymagania funkcjonalne i niefunkcjonalne, tworzy epic, story dla epic, tworzy sprint i zadania, 
i to wszystko może się zmieniać, bo może zmienić się wymaganie, które wpłynie na epic a tym samym na story i sprint, wymaga to aktualizacji całego planu co jest ryzykowne, bo LLM może nie o czymś zapomnieć, czegos nie doczytać, i nie zaktualizować. Zadanie które zostały zrealizowane już nie mają znaczenia bo są historyczne i na nie zmiany wymagnań, albo nowe informacje oraz zmiany wprowadzane przez użytkownika nie wpływają, ale już na otwarte rzeczy albo w realizaji to już tak. I tu trzeba zadać sobie pytanie czy realizowane rzeczy muszą być aktualizowane, bo być moze zmiany będę dopiero wchodzić po zakonczeniu realizowanch zadań, a może jest tak że zmiany które wprowadzamy dopiero chcemy zacząć wprowadząć za jakiś czas, czyli teraz chcemy zrobić X, Y, ale za jakiś czas chcemy zmienić Y na coś troche innego na Z, więc zmiana funkcjonalna ktora doszła dziś, nie ma jeszcze znaczenia dla otwartych zadań, bo będziemy wdrażać to kiedyś bo na ten moment mamy taki zakres projektu , a w następnych etapach ten zakres będzie inny i to jest duze ryzyko jak to śledzić, jak mapować, jak zapysywać by LLM mógł to łatwo czytać i rozumieć i się nie pogubić. Do tego możemy weryfikować deep-feasibility dla całego planu (dla naszej listy zadań) czy osiagniemy to co chidentyfikować,)

Ważną rzeczą jest że jak już mamy projekt i dużo kodu, to zadania zamknięte i zakończne to raczej czytać nie będziemy, więc jeżeli dojdą nowe wymagania, nowe rzeczy do zrobienia , to kod (projekt) może być tak skomplikowany ze LLM nie przewidzi gdzie i co trzeba zmienićcemy tą listą kroków, bo jeżeli zamienimy BMM w zapis działań i rozbijemy to na zadania na liście to też będzie to łatwiej przewidywać (tak mi się wydaje, moze jakies ryzyka )

Epici, Story, Sprint, zadania to jest sposób dojścia od PRD,architektury, i wymagań i potrzeb użytkownika do realnego kodu, jest to forma transformacji 
[Kod projektu] = Epic-Story-Sprint([PRD, architektura, wymagania]) , ale jest to mało precyzyjne, i w samo w spobie jest zagadnieniem jak to kontrolować, jak kontrolować zmiany w epicach, jak kotrnolować wymagania 
[Potrzeba_użytkownika] = użytkwonik deklaruje potrzebję , potrzeba wpływa na architekturę, byc może mieliśmy już [Architektura_1], [Architektura_2] które łączą się z określonymi [PRD_1], [PRD_2], mozę z jakimiś potrzebami użytkownika [Potrzeba_użytkownika_1], [Potrzeba_użytkownika_2]
[Architektura_3] = deep-architecture([PRD_1],[Potrzeba_użytkownika_1]) - pytanie jest co jest pierwsze, wymagania funkcjonalne i niefunkcjonalne czy architektura, albo równoczęsnie, tu jest dużo do przemyślenia, tu są ryzyka jak notacja powinna wygladać 
[Wymaganie_1] = deep-requirements([PRD],[Architektura],[Potrzeba_użytkownika]) 
[Epic_1] = deep-plan([PRD],[Architektura],[Wymaganie_1], [Wymaganie_2])
[kawałek kodu projektu] = deep-develop([Epic_1])

inna sprawa żę poszczególe kroki (scenariusze) opisane w BMM jak C:\Users\lukasz.krysik\Desktop\deep-verify\deep-verify\_bmad\bmm\workflows\2-plan-workflows\create-prd czyli tworzenie prd to są jakieś funkcje , moze powinno powstać deep-prd które przyjmuje pewne wartości czyli na przykład deep-prd jest to zbiór kroków i działań ta funkcja 
deep-prd([pomysł])
deep-prd to tak naprawdę zrbiór:
[Potrzeba_użytkownika] = użytkwonik deklaruje potrzebję , potrzeba wpływa na architekturę, byc może mieliśmy już [Architektura_1], [Architektura_2] które łączą się z określonymi [PRD_1], [PRD_2], mozę z jakimiś potrzebami użytkownika [Potrzeba_użytkownika_1], [Potrzeba_użytkownika_2]
[Architektura_3] = deep-architecture([PRD_1],[Potrzeba_użytkownika_1]) - pytanie jest co jest pierwsze, wymagania funkcjonalne i niefunkcjonalne czy architektura, albo równoczęsnie, tu jest dużo do przemyślenia, tu są ryzyka jak notacja powinna wygladać 
[Wymaganie_1] = deep-requirements([PRD],[Architektura],[Potrzeba_użytkownika]) 
[Epic_1] = deep-plan([PRD],[Architektura],[Wymaganie_1], [Wymaganie_2])

tylko mam jeden problem, że w tworzeniu prd mamy dobrze opisane kroki step-02-discovery.md, step-03-success.md, step-04-journeys.md, step-05-domain.md, ktore są krokami postępowań , może należy to lepiej opisać niż wyżej 
że deep-prd to procedura skladajaca się z 
składająca sie z procedur discovery, success, journeys, domain
czyli mamy procedurę którą opiszemy jako {deep-prd} wykonujacą procedury {discovery}, {success}, {journeys}, {domain} ... itd 
a procedura {discovery} składa sie z kroków takich i takich opisanych w prd_discovery.md 
{success} = prd_success.md 

To są wolne przemyślenia ale chciałbym żeby to jakoś wymyślić, by móc to rozbić na zapis taki ktory jest lepszy, w ktorym mogę kontrolować co zostalo wykonane, co można następne w kolejnosci wykonać a nie ma żadnych zależności itd, 
pytanie jak taka lista będzie zachowywać się przy zmianach wymagań, jak tym zarządzać, jest to ryzyko, jak wersonować zmiany żeby je uwidaczniać, co i kiedy się zmieniło i dlaczego, skąd wynika ta zmiana (czym spowodowana), jak wersjnować wymagania fukcyjne i niefunkcyjne, jak zapewnić zeby to bylo łatwe dla LLM i czytelne dla użytkwonika 

mam takie odczucie że Epici, Story, Sprinty to są transformaty zamieniające wymagania, architekturę, prd na określony kod, 