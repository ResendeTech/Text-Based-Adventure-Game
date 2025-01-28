import curses

def create_menu(stdscr, moves):
    current_row = 0

    # Initialize color pair 1 to be cyan on black
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.clear()
    stdscr.refresh()

    while True:
        h, w = stdscr.getmaxyx()

        # Create windows for the attack choices and the description
        move_window = curses.newwin(h//2, w//2, 0, 0)
        info_window = curses.newwin(h//2, w//2, 0, w//2)

        # Draw a box around each window
        move_window.box()
        info_window.box()

        # Create pads for the attack choices and the description
        move_pad = curses.newpad(len(moves) + 3, w//2 - 2)
        info_pad = curses.newpad(len(moves) + 3, w//2 - 2)

        move_pad.clear()
        info_pad.clear()

        for idx, move in enumerate(moves):
            x = 2
            y = idx + 2
            if idx == current_row:
                move_pad.attron(curses.color_pair(1))
                move_pad.addstr(y, x, move)
                move_pad.attroff(curses.color_pair(1))

                description, damage = move_info[move]
                info_pad.addstr(2, 2, f"Description: {description}")
                info_pad.addstr(4, 2, f"Damage: {damage}")
            else:
                move_pad.addstr(y, x, move)

        # Refresh the pads
        move_pad.refresh(0, 0, 1, 1, min(h//2, len(moves) + 3), min(w//2, w) - 2)
        info_pad.refresh(0, 0, 1, w//2 + 1, min(h//2, len(moves) + 3), w - 2)

        # Overlay the pads onto the windows
        move_window.refresh()
        info_window.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(moves)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.addstr(0, 0, "You selected '{}'".format(moves[current_row]))
            stdscr.refresh()
            stdscr.getch()
            break

def main():
    moves = ["Basic Attack", "Strong Attack", "Mega Attack", "Ultra Attack"]
    curses.wrapper(create_menu, moves)

if __name__ == "__main__":
    main()