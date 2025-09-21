
Projet Portafolio

BLOCK 1, FRONTEND

----------------------------------------------------------------------------------------------------------------

Dans cette partie, je vais créer un site statique (ladingpage HTML+CSS).

Je vais essayer de utiliser la semantique correcte pour html, en contant avec les bonnes practiques SEO, pour google.
Aussi je le fais en mode responsive, pour resolutions mobile et pc

Premier je vais commencer faire le mode mobile, adjuster tout a la petite resolution, et apres en ecran complet qui profite 
toute l'espace del container selons la proportion de pixelles sur l'ecran

------------------------------------------------------------------------------------------------------------------

Je vais commencer pour le page 'home', je crois cest la plus complexe, une fois finis, les autres serais plus vite (c/p).

Le header je vais le former avec une barre de navigation (navbar) et des liens (hypertexte) pour changer d'onglet/sections.
Je fais apres un hero, comme presentation avec une img et un lien pour regarder les ouvres du portafolio.
Un banner, pour montrer le contacte (address ,telf...)

Une section avec des cards pour monstrer les services et apres les monstrer aussi apres une image.
Une presentation des projets realisés, avec un scroll horizontel.

Une section simple avec les events
Encore une autre section avec des cards, et des liens pour de notices

Et pour finir, un footer avec un label pour introduir le email, les donnes de contacte, et des liens d'interet

-------------------------------------------------------------------------------------------------------------------

Tout ça, avec son style sur css, sans framework.

Je essayé de utiliser des parametres global, pour pas repeter bcp de code.
Comme les fonts, les buttons, le hover pour les buttons, la taille des containers...
Aussi je vais essayer de reagrouper les classes avec les memes parametres/atributes pour repeter le minimun.

Pour le hero, je vais metre une image de background, utilisant gradient, pour obscure l'image et faire le contrast.
Pour les cards, je voulais le faire gradient aussi, parce que on peut faire une espece de degradée , mais jai eu des problemes avec, et
finalement je utilisé un background (black avec 0.5 de opacité) et un z-index (pour positiioner le background abajo de le contenu de la card).
Comme ça, je laisse l'estyle de la card fixé, et si je besoin changer l'image, il faut que toucher le path de la img et cest tout.



