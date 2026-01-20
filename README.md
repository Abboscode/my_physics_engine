# my_physics_engine

To do 
First define view plane which is x and y plane 
how to do it ?
and then compute projectoon of all point in 3d to 2d plane
1. Using the Normal Vector (Orthogonal Complement) If the plane is defined by a unit normal vector \(\mathbf{n}\) and a point \(\mathbf{r}_{\mathbf{0}}\) on the plane, the projection \(\mathbf{p}^{\prime }\) of point \(\mathbf{p}\) is found by subtracting the point's "height" above the plane from itself. Vector Formulation:\(\mathbf{p}^{\prime }=\mathbf{p}-((\mathbf{p}-\mathbf{r}_{\mathbf{0}})\cdot \mathbf{n})\mathbf{n}\)If \(\mathbf{n}\) is not a unit vector, normalize it or use:\(\mathbf{p}^{\prime }=\mathbf{p}-\frac{(\mathbf{p}-\mathbf{r}_{\mathbf{0}})\cdot \mathbf{n}}{\|\mathbf{n}\|^{2}}\mathbf{n}\)

`![projection](https://latex.codecogs.com/svg.image?\dpi{120}\mathbf{p}=\mathbf{r}_0-(\mathbf{n}\cdot(\mathbf{r}-\mathbf{r}_0))\mathbf{n})`