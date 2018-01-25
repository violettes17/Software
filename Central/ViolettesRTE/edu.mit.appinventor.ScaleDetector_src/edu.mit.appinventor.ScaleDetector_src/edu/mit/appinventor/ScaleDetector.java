// -*- mode: java; c-basic-offset: 2; -*-
// Copyright 2009-2011 Google, All Rights reserved
// Copyright 2011-2012 MIT, All rights reserved
// Released under the Apache License, Version 2.0
// http://www.apache.org/licenses/LICENSE-2.0


package edu.mit.appinventor;

import android.content.Context;
import android.util.Log;
import android.view.ScaleGestureDetector;
import android.view.ScaleGestureDetector.SimpleOnScaleGestureListener;

import com.google.appinventor.components.annotations.DesignerComponent;
import com.google.appinventor.components.annotations.PropertyCategory;
import com.google.appinventor.components.annotations.SimpleEvent;
import com.google.appinventor.components.annotations.SimpleFunction;
import com.google.appinventor.components.annotations.SimpleObject;
import com.google.appinventor.components.annotations.SimpleProperty;
import com.google.appinventor.components.common.ComponentCategory;

import com.google.appinventor.components.runtime.AndroidNonvisibleComponent;
import com.google.appinventor.components.runtime.Canvas;
import com.google.appinventor.components.runtime.ComponentContainer;
import com.google.appinventor.components.runtime.EventDispatcher;


/**
 * This example demonstrates how to add a new gesture detector to App Inventor
 * using App Inventor extensions. It creates a component called ScaleDetector.
 * ScaleDetector is used in conjunction with a Canvas.  It provides a When Scale
 * event hander that fires when there is a scale gesture (e.g. a two-finger pinch) on the
 * canvas.
 * Once could use a similar
 * technique to create other extensions that add other kinds of gesture detectors and 
 * handlers to canvases.
 *
 */
@DesignerComponent(version = 1,
		   description = "A ...",
   category = ComponentCategory.EXTENSION,
   nonVisible = true,
   iconName = "images/extension.png")
@SimpleObject(external = true)
public class ScaleDetector extends AndroidNonvisibleComponent {
 

  // the Canvas on which to install the scale detector
  private Canvas myCanvas;
  /**
   * Creates a Scale Detector component for installing on a Canvas
   * 
   * @param container container, component will be placed in
   */
  public ScaleDetector(ComponentContainer container) {
    super(container.$form());
    
  }

  /**
   * Input is the canvas component on which to install the detector
   */
  @SimpleFunction
  public void AddHanderToCanvas(Canvas myCanvas) {
    this.myCanvas = myCanvas;
    // The key step here is to create the gesture detector and register it for the Canvas
    // the gesture detector is created from a gesture listener.  The activity context for detection
    // the will be the context of the canvas.
    ExtensionScaleDetector myDetector = 
        new ExtensionScaleDetector(myCanvas.getContext(), new MyOnScaleGestureListener());
    myCanvas.registerCustomGestureDetector(myDetector); 
  }

  @SimpleProperty(category = PropertyCategory.BEHAVIOR)
  public Canvas MyCanvas() {
    return myCanvas;
  }
  
 @SimpleEvent
  public void Scale(double scaleFactor) {
    EventDispatcher.dispatchEvent(this, "Scale", scaleFactor);
  }
  
 // The gesture detector to be added should extend an ordinary Android gesture detector, and
 // also implement the Canvas.ExtensioGestureDetector interface
 // It's created from a gesture listener and an activity context
 public class ExtensionScaleDetector extends ScaleGestureDetector 
         implements Canvas.ExtensionGestureDetector {
   public ExtensionScaleDetector(Context c, OnScaleGestureListener l ) {
     super(c,l);
   }
 }

 // Here's the gesture listener. 
 
 public class MyOnScaleGestureListener extends
            SimpleOnScaleGestureListener {
 
   //  We override the event handling of the ordinary SimpleOnScaleGestureListener
   // In this case, make the onSlcale event call the component's Scale event handler, whose
   // behavior can be defined by the When Scale block.
   @Override
   public boolean onScale(ScaleGestureDetector detector) {          
     float scaleFactor = detector.getScaleFactor();
    //  Log.i("Scale", "onScale was signaled, scale factor = " + scaleFactor);
     Scale((double) scaleFactor);
     return true;
   }

   // Similar to Scale, we could create BeginScale and EndScale blocks and signal them here,
   // but we'll forego that for this simple demo
   @Override
   public boolean onScaleBegin(ScaleGestureDetector detector) {
     return true;
   }

   @Override
   public void onScaleEnd(ScaleGestureDetector detector) {
   }
 }




}

