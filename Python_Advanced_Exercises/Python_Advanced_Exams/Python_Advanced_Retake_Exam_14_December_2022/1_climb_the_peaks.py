from collections import deque

TOTAL_PEAKS = 5

food_portions = [int(x) for x in input().split(', ')]
stamina = deque(int(x) for x in input().split(', '))

peaks_data = deque([
    ('Vihren', 80),
    ('Kutelo', 90),
    ('Banski Suhodol', 100),
    ('Polezhan', 60),
    ('Kamenitza', 70),
])

conquered_peaks = []
is_succeeded = False

while food_portions:
    daily_portion = food_portions.pop()
    daily_stamina = stamina.popleft()
    total_daily_energy = daily_portion + daily_stamina

    if peaks_data:
        peak_name, peak_level = peaks_data[0]

        if total_daily_energy >= peak_level:
            conquered_peaks.append(peak_name)
            peaks_data.popleft()

            if len(conquered_peaks) == TOTAL_PEAKS:
                is_succeeded = True
                break

if is_succeeded:
    print('Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print('Alex failed! He has to organize his journey better next time -> @PIRINWINS')

if conquered_peaks:
    print(f'Conquered peaks: ')
    print("\n".join(conquered_peaks))