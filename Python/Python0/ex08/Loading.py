import time
import sys
import os

def ft_tqdm(iterable, fill='█'):
    delta = 1
    last_percent = 0
    total = len(iterable)
    if total == 0:
        sys.stdout.write('0it [00:00, ?it/s]\n')
        return
    start_time = time.time()
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80
    length = terminal_width - 40
    def print_progress_bar(iteration):
        nonlocal last_percent
        elapsed_time = time.time() - start_time
        speed = iteration / elapsed_time if elapsed_time > 0 else 0
        percent = int(100 * (iteration / (total)))
        if percent >= last_percent + delta:
            last_percent = percent
            filled_length = int(length * iteration // total)
            bar = fill * filled_length + '-' * (length - filled_length)
        
            remaining_time = (elapsed_time / iteration) * (total - iteration) if iteration > 0 else 0
            eta = time.strftime('%M:%S', time.gmtime(remaining_time))

            elapsed_str = time.strftime('%M:%S', time.gmtime(elapsed_time))

            sys.stdout.write(f'\r{percent}%|{bar}| {iteration}/{total} '
                         f'[{elapsed_str}<{eta}, {speed:0.2f}it/s]')
            sys.stdout.flush()

    for i, item in enumerate(iterable):
        print_progress_bar(i + 1)
        yield item
    sys.stdout.write('\n')

