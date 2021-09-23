module speakerGroove() {
  cube(size=[23, 23, 3]);
  translate([7, 7, 3]) {
    cube(size=[9, 16, 1.5]);
  }
  translate([0, 16, 3]) {
    cube(size=[23, 7, 1.5]);
  }
  for(i=[3:16/7*2:19]) {
    translate([3, i, -3]) {
      cube(size=[17, 2.5, 3]);
    }
  }
}

module standbase() {
  difference() {
    union() {
      // base
      cube([170, 80, 5]);

      // steps
      intersection(){
        union() {
          union() {
            translate([85, 100, 5]){
              cylinder(r=60, h=1);
            }
            translate([0, 120, 5]){
              cylinder(r=80, h=1);
            }
            translate([170, 120, 5]){
              cylinder(r=80, h=1);
            }
          }
          union() {
            translate([85, 100, 6]){
              cylinder(r=58, h=1);
            }
            translate([0, 120, 6]){
              cylinder(r=78, h=1);
            }
            translate([170, 120, 6]){
              cylinder(r=78, h=1);
            }
          }
          translate([85, 100, 7]){
            cylinder(r=56, h=1);
          }
          translate([85, 100, 8]){
            cylinder(r=54, h=1);
          }
        }
        translate([0, 0, 5]) {
          cube([170, 80, 5]);
        }
      }
    }
    translate([85, -160, 0]) {
      for(i=[0:12:360]) {
        rotate([0, 0, i]) {
          translate([194.5, 0, 0]) {
            cylinder(r=3, h=10, center=true, $fn=60);
          }
        }
      }
    }
    translate([26.5, 57, 4.5]) {
      rotate([0, 180, 0]) {
        speakerGroove();
      }
    }
    translate([166.5, 57, 4.5]) {
      rotate([0, 180, 0]) {
        speakerGroove();
      }
    }
  }
}


module mainDisplay() {
  difference() {
    // base
    cube([55, 25, 3]);
    // minus
    translate([1, 1, 2]) {
      cube([53, 23, 1]);
    }
  }
  translate([7, -10, 0]) {
    cube([3, 10, 3]);
  }
  translate([45, -10, 0]) {
    cube([3, 10, 3]);
  }
}

module bardeco() {
  difference() {
    // base
    cube([8, 27, 2]);
    // minus
    translate([2, 0, 1]){
      cube([1, 27, 1]);
    }
    translate([5, 0, 1]){
      cube([1, 27, 1]);
    }
  }
  translate([0, -9, 0]) {
    cube([2, 9, 2]);
  }
  translate([6, -9, 0]) {
    cube([2, 9, 2]);
  }
}

module bigheart2d() {
  difference() {
    // base
    union() {
      rotate([0, 0, 25]) {
        scale([0.7, 1, 1]) {
          circle(r=30);
        }
      }
      translate([13, 0, 0]){
        rotate([0, 0, -25]) {
          scale([0.7, 1, 1]) {
            circle(r=30);
          }
        }
      }
    }
    // minus
    union() {
      rotate([0, 0, 25]) {
        scale([0.7, 1, 1]) {
          circle(r=22);
        }
      }
      translate([13, 0, 0]){
        rotate([0, 0, -25]) {
          scale([0.7, 1, 1]) {
            circle(r=22);
          }
        }
      }
    }
    translate([7, -23, 0]) {
      square(size=[60, 30], center=true);
    }
  }
}

module bigheart3d() {
  linear_extrude(height=5) {
    scale([1.2, 1.2, 1.2]){
      translate([0, 2, 0]) {
        bigheart2d();
      }
    }
  }
  translate([-19, -7, 2.5]) {
    rotate([90, 0, 0]) {
      cylinder(h=9 ,r=2);
    }
  }
  translate([35, -7, 2.5]) {
    rotate([90, 0, 0]) {
      cylinder(h=9 ,r=2);
    }
  }
}

module heart2d() {
  difference() {
    union() {
      translate([-1, 0, 0]) {
        rotate([0, 0, 30]) {
          scale([0.7, 1, 1]) {
            circle(r=5);
          }
        }
      }
      translate([1, 0, 0]) {
        rotate([0, 0, -30]) {
          scale([0.7, 1, 1]) {
            circle(r=5);
          }
        }
      }
    }
    union() {
      translate([-1, 0, 0]) {
        rotate([0, 0, 30]) {
          scale([0.7, 1, 1]) {
            circle(r=3);
          }
        }
      }
      translate([1, 0, 0]) {
        rotate([0, 0, -30]) {
          scale([0.7, 1, 1]) {
            circle(r=3);
          }
        }
      }
    }
  }
}

module clover2d() {
  for (deg = [0:120:240]) {
    rotate([0, 0, deg]) {
      translate([0, 4.5, 0]) {
        heart2d();
      }
    }
    
  }
}

module clover3d() {
  linear_extrude(height=2) {
    clover2d();
  }
}

module logo() {
  rotate([0, 0, -10]) {
    clover3d();
  }
  translate([0, 0, 2]) {
    rotate([0, 0, 10]) {
      clover3d();
    }
  }
  translate([0, 0, -2.5]) {
    cylinder(r=2, h=5, center=true);
  }
}

module petitDisplay() {
  difference() {
    cube([35, 15, 2]);
    translate([1, 1, 1]) {
      cube([33, 13, 1]);
    }
  }
}

module sidedeco() {
  translate([2.5, 3, 3]) {
    petitDisplay();
  }
  for(x = [0:37/5:37]) {
    translate([x, -4, 0]) {
      if (x == 0 || x == 37){
        translate([0, -7, 0]) {
          cube([3, 32, 3]);
        }
      } else {
        cube([3, 25, 3]);
      }
    }
  }
  translate([0, 21, 0]) {
    cube([40, 3, 5]);
  }
}

module groove() {
  rotate([0, 0, 6]) {
    linear_extrude(height=3){
      difference() {
        circle(r=200, $fn=30);
        circle(r=189, $fn=30);
      }
    }
  }
}

module backdeco() {
  difference() {
    translate([-7.8, 0, 0]) {
      bigheart3d();
    }
    translate([0, 27, 5]) {
      logo();
    }
  }
}

// !backdeco();

// main render
difference() {
  color("#2f2f2f"){
    difference() {
      standbase();
      translate([85, -160, 2]){
        groove();
      }
    }
  }

  color("#88ddff"){
    translate([57.5, 68, 10]){
      rotate([90, 0, 0]){
        mainDisplay();
      }
    }
  }

  color("#ff88aa"){
    translate([46, 69, 9]) {
      rotate([90, 0, 0]){
        bardeco();
      }
    }
    translate([116, 69, 9]) {
      rotate([90, 0, 0]){
        bardeco();
      }
    }
  }

  color("#eedd55"){
    translate([85, 78, 17]){
    // translate([0, -50, 14]){
      rotate([90, 0, 0]) {
        backdeco();
      }
    }
  }

  color("#00ff55"){
    translate([85, 73, 44]) {
      rotate([90, 0, 0]) {
        logo();
      }
      
    }
  }

  color("#5577ff") {
    translate([0.5, 55, 11]) {
      rotate([90, 0, 15]) {
        sidedeco();
      }
    }
    translate([130, 65, 11]) {
      rotate([90, 0, -15]) {
        sidedeco();
      }
    }
  }
}

*mainDisplay();
*bardeco();
*backdeco();
*logo();
*sidedeco();