package com;

public class ShapeFactory {

    public static Shape getShape( String Shape){
        if(Shape.equals("Circle")){
            return new Circle();
        }else if(Shape.equals("Rectangle")){
            return new Rectangle();
        }else{
            return null;
        }
    }
}
