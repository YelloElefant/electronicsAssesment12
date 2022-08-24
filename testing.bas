main:
readadc b.2, b2 ;left hand
readadc b.1, b1 ;right hand
;debug
if b2 < 18 then right
if b1 < 18 then left

goto f

goto main



f:
high c.0
high b.5
pause 200
low b.5
low c.0
goto main

right: ;power right
high b.5
low c.0
pause 50
low b.5
goto main

left: ;power left
high c.0
low b.5
pause 50
low c.0
goto main