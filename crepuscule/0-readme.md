:pencil2:  Pensez à contribuer à cette page --- [login hackmd](https://hackmd.io/) 

:arrow_forward:   [graph plein ecran](https://botapad.padagraph.io/import/igraph.html?s=https://hackmd.io/2IuIeln8RtWv2pNWCf2W5A&bgcolor=EEE&vtx_size=1)  --- [chat](https://gitter.im/padagraph/cafe)  --- [conference](https://appear.in/padagraph) 


---
# crépuscule 

Crepuscule tente de représenter les conflits d’intérêts
mis en évidence par l’écrit “Crépuscule” de Juan Branco.

>Il y a pire que celui qui menace,
>que celui tabasse, que celui qui intimide,
>ils a ceux qui arme les esprits
>pour légitimer les violences dans notre pays.

https://www.facebook.com/juan.branco.98/videos/748020525569936/

---
### Chat 

ouvrir un chat gitter padagraph: https://gitter.im/padagraph/cafe 
par contre il faut être loggué avec `github` ou `twitter`.

### visio conference jusqu'a 4 personnes
https://appear.in/padagraph


---
### les bugs avec les données
Comment éviter les bugs de transparence.

* mettre une valeur par defaut dans les colonne 
    > `size[0.5]` entre 0 et 1 
    > `shape[triangle]` circle, square, diamond, triangle-top, triangle-bottom
  
* verifier que toutes les cellules sont renseignées qd la colonne `label` existe.

* il est possible d'utiliser le `label` comme `id`
    > @Media: #label
* Attention a ne pas mettre d espace dans les `id` [à vérifier]


---
### Proposition de colonne

**@Personnes** 
* fortune, Salaire,
* mise en examen, condamnation
* lien wikipedia
* extrait du livre


---

### Relations
Pour les relations, on a changé un peu la syntaxe pour introduire la "mise en relation". 

Il en existe donc de 2 sortes:
1) les relations de un à un, du type : un_tel a financé cette_entreprise
2) les relations de un à plusieurs, du type un_tel a introduit _lui_et_elle_et_lui
Deux exemples qui sont dans le dossier relations... 

Il est bien sûr possible de créer de nouveaux types de relations.

Il y a aussi les événements, qui sont en eux même des relations (genre un repas avec des participants, ou une affaire judiciaire...)

---

### Questions

...