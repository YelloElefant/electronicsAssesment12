main:
readadc b.4, b2 ;left hand
readadc b.5, b1 ;right hand
debug
if b2 < 18 then right
if b1 < 18 then left
if b1 < 18 and b2 < 18 then s
goto f

goto main



f:
let b8 = 1
let b9 = 0
high c.4
high c.1
pause 200
goto main

;back:
;low c.0
;high c.4
;let b8 = 0
;let b9 = 1
;pause 200
;goto main


s: ;stop
low c.4
low c.1
pause 200
goto main

right: ;power right
high c.4
low c.1
pause 50
goto main

left: ;power left
high c.1
low c.4
pause 50
goto main