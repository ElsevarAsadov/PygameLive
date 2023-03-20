
## About

This module provides live coding in pygame.You can see your code changes at once without restart application.

![](https://files.fm/u/yskzc59xk)

> **Note:** Your Game should be implemented OOP style.
## Example Game

Example game (FlappyDooM) is made by Stanislav Petrov [StanislavPetrovV](https://github.com/StanislavPetrovV). 

![alt text](https://github.com/StanislavPetrovV/FlappyDooM/raw/main/screenshot/0.jpg)

You should design your game like this to work PygameLive properly(highly recommended to look up example folder):

```mermaid
graph LR

B(Game Object 1) --> C(Main Renderer)
D(Game Object 2) --> C(Main Renderer)
E(Game Object 3) --> C(Main Renderer)
```
> **Note:** PygameLive only can be used for your main **draw**, **update**, **event** handler methods.