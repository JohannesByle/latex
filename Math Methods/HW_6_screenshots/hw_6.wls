#!/usr/bin/env wolframscript
(* ::Package:: *)

Clear[x,v,energy,dotenergy];
ndiv=20;
dt = (8 Pi)/ndiv;
v[n_]:=v[n]=v[n-1]-x[n-1] dt;
v[0]=0;
x[n_]:=x[n]=x[n-1]+v[n-1] dt;
x[0]=1;
ListPlot[Table[{x[t],v[t]},{t,0,ndiv}]]
energy[n_]:=energy[n]=(x[n]^2+v[n]^2)/2
ListPlot[Table[energy[t],{t,0,ndiv}]]
dotenergy[n_]:=dotenergy[n]=(energy[n+1]-energy[n])/dt
ListPlot[Table[dotenergy[t],{t,0,ndiv}]]


(* ::InheritFromParent:: *)
(**)
(*Graphics[{{}, {}}, AspectRatio -> GoldenRatio^(-1), Axes -> {True, True}, AxesLabel -> {None, None}, AxesOrigin -> {0, 0}, DisplayFunction -> Identity, Frame -> {{False, False}, {False, False}}, FrameLabel -> {{None, None}, {None, None}}, FrameTicks -> {{Automatic, Charting`ScaledFrameTicks[{Identity, Identity}]}, {Automatic, Charting`ScaledFrameTicks[{Identity, Identity}]}}, GridLines -> {None, None}, GridLinesStyle -> Directive[GrayLevel[0.5, 0.4]], ImagePadding -> All, Method -> {"DefaultBoundaryStyle" -> Automatic, "DefaultGraphicsInteraction" -> {"Version" -> 1.2, "TrackMousePosition" -> {True, False}, "Effects" -> {"Highlight" -> {"ratio" -> 2}, "HighlightPoint" -> {"ratio" -> 2}, "Droplines" -> {"freeformCursorMode" -> True, "placement" -> {"x" -> "All", "y" -> "None"}}}}, "DefaultMeshStyle" -> AbsolutePointSize[6], "ScalingFunctions" -> None, "CoordinatesToolOptions" -> {"DisplayFunction" -> ({(Identity[#]& )[Part[#, 1]], (Identity[#]& )[Part[#, 2]]}& ), "CopiedValueFunction" -> ({(Identity[#]& )[Part[#, 1]], (Identity[#]& )[Part[#, 2]]}& )}}, PlotRange -> {{0, 1}, {0., 0.}}, PlotRangeClipping -> True, PlotRangePadding -> {{Scaled[0.02], Scaled[0.02]}, {Scaled[0.05], Scaled[0.05]}}, Ticks -> {Automatic, Automatic}]*)


Clear[x]
Clear[v]
Clear[energy]
Clear[dotenergy]
dt = 0.1;
v[n_]:=v[n]=v[n-1]-x[n-1] dt;
v[0]=0;
x[n_]:=x[n]=x[n-1]+v[n] dt;
x[0]=1;
ListPlot[Table[{x[t],v[t]},{t,0,20000}]]
energy[n_]:=energy[n]=(x[n]^2+v[n]^2)/2
ListPlot[Table[energy[t],{t,0,20000}]]
dotenergy[n_]:=dotenergy[n]=(energy[n+1]-energy[n])/dt
ListPlot[Table[dotenergy[t],{t,0,20000}]]



