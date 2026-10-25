Jack Rabbits

Chaque joueur pose un lapin sur une case vide. À chaque tour, tous les lapins du plateau se reproduisent : ils prennent les cases vides juste à côté d'eux (haut, bas, gauche, droite). Le jeu s'arrête quand le plateau est plein.

Le code est séparé en plusieurs fonctions : NewBoard crée le plateau, displayBoard l'affiche, possibleSquare et selectSquare s'occupent de la saisie et de la validité d'un coup, updateBoard fait le tour de jeu, again regarde s'il reste une case libre et jackRabbits contient la boucle principale.

Dans updateBoard on fait d'abord une copie du plateau avec copy.deepcopy. On lit l'ancien plateau mais on écrit dans la copie, comme ça un lapin qui vient d'apparaître ne se reproduit pas tout de suite dans le même tour. Pour chaque lapin on remplit ses voisins vides dans la copie. Si les deux joueurs veulent la même case, c'est celui qui vient de jouer qui l'obtient. Ensuite on recopie la copie dans le plateau et on pose le nouveau lapin, qui ne se reproduira qu'au tour suivant.

Dans jackRabbits, une variable turn augmente à chaque tour : impair pour le joueur 1, pair pour le joueur 2. On boucle tant que again renvoie vrai, et à la fin on affiche le perdant selon la parité de turn.
 
Attract

Chaque joueur pose un pion sur une case vide, et ce pion attire d'une case les pions qui sont sur sa ligne et sur sa colonne. Le jeu s'arrête quand le plateau est plein, et la taille doit être paire.

NewBoard crée le plateau et redemande la taille tant qu'elle est impaire, displayBoard s'occupe seulement de l'affichage, possible dit si un coup est valide, et selectSquare demande les coordonnées au joueur en utilisant possible, attract_pions contient la règle propre au jeu, updateBoard fait un coup complet (pose du pion, attraction, affichage), again vérifie s'il reste une case vide et Attract contient la boucle principale.

Pour attract_pions, on part du pion qui vient d'être posé en (i, j) et on fait quatre parcours : vers la gauche, la droite, le haut et le bas. Dans chaque sens on commence par la case la plus proche du pion posé et on s'en éloigne. Si une case contient un pion et que la case juste avant (côté pion posé) est vide, on le déplace d'un cran. Comme on commence par les plus proches, une case libérée peut être prise tout de suite par le pion suivant, donc une rangée de pions avec des trous avance d'un cran d'un coup. Les pions déjà collés au pion posé ne bougent pas, et les diagonales ne sont pas touchées.

Dans la boucle principale, turn impair c'est le joueur 1 et pair le joueur 2. Après chaque tour on regarde les cases à l'intérieur du plateau : si une case a ses quatre voisines en diagonale occupées par l'autre joueur, on augmente un compteur. À la fin on compare les compteurs pour afficher le gagnant ou un match nul.
