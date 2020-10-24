# PHP Array 

```
array();
```
Trong PHP có 3 mảng : 
- Mảng được lập chỉ mục 
- Mảng kết hợp
- Mảng nhiều chiều 

Lấy chiều dài của 1 mảng 

```
<?php
$cars = array("Volvo", "BMW", "Toyota");
echo count($cars);
?>
```

Có 2 cách tạo 1 mảng số

```
<html>
   <body>
   
      <?php
         /* First method to create array. */
         $numbers = array( 1, 2, 3, 4, 5);
         echo "$numbers <br />";
         
         /* Second method to create array. */
         $number[0] = "one";
         $number[1] = "two";
         $number[2] = "three";
         $number[3] = "four";
         $number[4] = "five";
         echo "$number <br />";
      ?>
      
   </body>
</html>
```

Có 2 cách tạo mảng liên kết như sau : 

```
<html>
   <body>
      
      <?php
         /* First method to associate create array. */
         $salaries = array("mohammad" => 2000, "qadir" => 1000, "zara" => 500);
         
         /* Second method to create array. */
         $salaries['mohammad'] = "high";
         $salaries['qadir'] = "medium";
         $salaries['zara'] = "low";
      ?>
   
   </body>
</html>
```

Mảng kết hợp 

```
Bản thử trực tiếp
<html>
   <body>
      
      <?php
         $marks = array( 
            "mohammad" => array (
               "physics" => 35,
               "maths" => 30,	
               "chemistry" => 39
            ),
            
            "qadir" => array (
               "physics" => 30,
               "maths" => 32,
               "chemistry" => 29
            ),
            
            "zara" => array (
               "physics" => 31,
               "maths" => 22,
               "chemistry" => 39
            )
         );
         
         /* Accessing multi-dimensional array values */
         echo "Marks for mohammad in physics : " ;
         echo $marks['mohammad']['physics'] . "<br />"; 
         
         echo "Marks for qadir in maths : ";
         echo $marks['qadir']['maths'] . "<br />"; 
         
         echo "Marks for zara in chemistry : " ;
         echo $marks['zara']['chemistry'] . "<br />"; 
      ?>
   
   </body>
</html>
```


