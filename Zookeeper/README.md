# Zookeeper

![Zoo](https://media.giphy.com/media/1gOadI4RGkrFpbMF7r/giphy.gif)

### About this project
Help the local zoo look after its denizens. You will create a tool for monitoring animals and their status.

### Run

Requirements:
- Python 3.7
- To run the tests: https://github.com/hyperskill/hs-test-python

`python zookeeper.py`

![Python projects](http://g.recordit.co/kXsziz4vBU.gif)


# Code it yourself: 

## 1. Rush into print
### Description
There are many animals in the zoo: all of them need care, and some of them are endangered and require preservation efforts. Animals must be fed, cleaned, surrounded by their kin, and kept happy. That is a difficult task for such a big open-range zoo, so one of your employers suggested a better way to accomplish that. She wants to be able to watch any animal on the screen with the help of a special program.

In this project, you will create a program that helps the zookeeper check on the animals and see that they're well. Your product will be able to understand commands from the zoo staff and show the animals on the monitor.

### Objectives
To begin with, you should develop a simple printer. Your program must show the text from the output example.

### Example
Output:

```
I do love animals!
Start looking after animals...
Deer looks fine.
Bat looks happy.
Lion looks healthy.
```

## 2: Show me an animal!

### Description
The important thing about working with animals is watching them. We need to see the animals on the screen to know how they are doing, right? At this time, we are ready to print something awesome: animal images! 

### Objectives
In the second stage, you need to develop an animal printer. Your program should show a certain animal: you will find it in the code field.

Please, don't remove the r character at the start of the code template. It's a part of the string and it's important. So, the string should start with r""" sequence.

### Example

Your output should contain the following ASCII image:

```
Switching on camera from the habitat with camels...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Yey, our little camel is sunbathing!
```

## 3: What's inside?

### Description

The third stage brings new abilities for your software: it will be able to recognize the number of a specific habitat from the input and show the animals living there.

Add all variables with images from the template to a variable with the type list. The order of variables matters: they must be in the order they're defined in the code. The list must contain all of them with no duplicates.

### Objectives

In this stage, your program should:

1. Ask for a number of the habitat using the following phrase: Which habitat # do you need?.
2. Use the input number as an index of your habitat to print its content.
3. End with the following phrase:
`The end of the program. To check another habitat restart the watcher please.`

### Examples

The greater-than symbol followed by a space (> ) represents the user input. Notice that it's not part of the input.

Example 1

```
Which habitat # do you need? > 5

Switching on camera from the habitat with rabbits...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
It seems there will be more rabbits soon!
---
The end of the program. To check another habitat restart the watcher please.
```

Example 2

```
Which habitat # do you need? > 4

Switching on camera from the habitat with bats...
_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\  W  //           <
       /             /~---~\             \
      /_            |       |            _\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\
                ~-. /  \_/  \ .-~
                   V         V
It looks like this bat is fine.
---
The end of the program. To check another habitat restart the watcher please.
```

## 4: Sustainable care <3

### Description

It's time to make your project more convenient and understandable. In this final stage, your software will be ready for use by the zoo staff. Your program should understand the habitat numbers, show the animals, and be able to work infinitely.

### Objectives

These are your tasks at this point:

1. Your program should repeat the behavior from the previous stage, now in a loop.
2. Do not forget to add an exit opportunity for the program: inputting the word exit must terminate the program.
3. At the end of execution, it must print `See you!`.

### Example

The greater-than symbol followed by a space (> ) represents the user input. Notice that it's not part of the input.

The complete program should work this way:

```shell script
Which habitat # do you need? > 3

Switching on camera from the habitat with a lovely goose...
	
                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \
 <_  `     (  <`<            \              `-._\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
This bird stares intently at you... (Maybe it's time to change the channel?)
> Which habitat # do you need? > 1

Switching on camera from the habitat with lions...
                                               ,w.
                                             ,YWMMw  ,M  ,
                        _.---.._   __..---._.'MMMMMw,wMWmW,
                   _.-""        '''           YP"WMMMMMMMMMb,
                .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
           /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
          /  .'             /  (       .'  /     Ww._     `.  `"
         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
        (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
The lion is croaking!
Which habitat # do you need? > exit
See you!
```