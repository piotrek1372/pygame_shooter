# main.py

import pygame
import sys  # Użyjemy sys.exit do bezpiecznego zamknięcia aplikacji

# --- Inicjalizacja Pygame ---
# To musi być wywołane na początku, aby moduły Pygame działały poprawnie
pygame.init()

# --- Ustawienia Okna Gry (Stałe) ---
# Używamy WIELKICH LITER dla stałych, których nie będziemy zmieniać w trakcie gry
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME_TITLE = "Mój Pierwszy Shooter!"
FPS = 60  # Klatki na sekundę

# --- Stworzenie Okna Gry ---
# screen to "płótno", na którym będziemy rysować
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(GAME_TITLE)

# --- Zegar (Clock) ---
# Clock pomoże nam kontrolować, ile razy na sekundę pętla gry się wykona
clock = pygame.time.Clock()

# --- Główna Pętla Gry (Game Loop) ---
running = True
while running:
    # 1. OBSŁUGA ZDARZEŃ (Input)
    # Pętla `for` przechodzi przez kolejkę wszystkich zdarzeń (ruchy myszki, klawisze, etc.)
    for event in pygame.event.get():
        # Sprawdzamy, czy gracz kliknął "X" w rogu okna
        if event.type == pygame.QUIT:
            running = False  # Kończymy pętlę i zamykamy grę

    # 2. AKTUALIZACJA STANU GRY (Update)
    # Na razie nic tu nie ma, ale tu będzie się ruszał gracz, wrogowie, itp.
    # ...

    # 3. RYSOWANIE (Render/Draw)
    # Wypełniamy całe tło jednolitym kolorem (Czarny w formacie RGB)
    # Robimy to w każdej klatce, aby "zmazać" poprzednią klatkę
    screen.fill((0, 0, 0))  # RGB: (Red, Green, Blue)

    # Tutaj w przyszłości będziemy rysować gracza, wrogów, pociski
    # ...

    # Aktualizacja wyświetlacza
    # `flip()` zamienia to, co narysowaliśmy "w tle", na główny ekran widoczny dla gracza
    pygame.display.flip()

    # Kontrola FPS
    # `clock.tick()` robi pauzę, aby cała pętla nie trwała krócej niż 1/60 sekundy
    # Gwarantuje to, że gra działa tak samo szybko na różnych komputerach
    clock.tick(FPS)


# --- Zakończenie Gry ---
# Gdy pętla `while running` się skończy, wychodzimy z gry
print("Zamykanie gry...")
pygame.quit()
sys.exit()