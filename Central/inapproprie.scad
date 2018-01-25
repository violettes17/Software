
outer = 1 ;
inner = outer * 0.9;
thickness = outer * 0.1;
feuilles = 11;
angle_feuille = 360/feuilles;
module interdit()
{

    rotate([0,0,-45]) union(){
        difference(){
            cylinder(r=1, h= thickness, $fn=100, center = true) ;
            cylinder(r=0.9, h= thickness, $fn=100, center = true) ;
            };
        cube( [2*inner,thickness,thickness], center = true);
    }

}


module feuille ()
{

    translate ([0,1,0]) scale([0.5,1]) intersection(){
            translate ([-outer/2,0,0]) cylinder(r=1, h= thickness/10, $fn=100, center = true) ;
            translate ([+outer/2,0,0]) cylinder(r=1, h= thickness/10, $fn=100, center = true) ;
            };
    
}

module pissenlit()
{
    for(i=[0:feuilles])
            {
            translate ([0,0,i*thickness/10]) rotate ([0,3,angle_feuille*i])
                {
                feuille();
                }
             };
}


material ("rouge") {interdit();};
material ("green") {scale(0.4)  pissenlit();};
