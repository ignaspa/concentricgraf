# concentricgraf
context:
This is a project I worked on to help create a new type
of data visualization with a group for BCB BioHacks 2018. (a hackathon put on by
the BioInformatics and Computational Biology Department at U of T)

objective:
We were given a lot of data on chromosome20 of the human
genome. We didn't understand much of it so we decided to try to make
an abstract data visualization format that could be applied to it.

our work:
We came up with a twist on a pie chart. Basically there would be
a series of concentric rings that would be characteristics
that would make up a circle. The circle would be split up into slices
and each slice would be an element. So in this case the slices were
genes and each ring would be a characteristic class that the gene may have
attributed to it. If the gene did have an attribute the slice of that
corresponding ring would be a color denoting it, and if not, then another color.
Futhermore we would use scikitlearn for principal component analysis (PCA)

http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html

to reduce the genes to a dimension of similarity, and then
have similar genes closer to each other on the circle. This is then a linear
form of comparison and so there must be a break/end point in the circle,
they cannot "loop in similarity".

my part:
I tried to implement the visualization using the python module pygame.
It turns out pygame was probably not the way to go (learning the har way!)
The arcs are gross, but the idea is still there.
