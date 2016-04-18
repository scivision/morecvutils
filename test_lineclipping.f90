program test

    use lineclip,only : sp,loop_cohensutherland,cohensutherland

implicit none



contains

logical function test_loop(Np)

integer, intent(in) :: Np
real(sp) :: length(Np)
real(sp) :: xmins(Np),ymaxs(Np),xmaxs(Np),ymins(Np)


real(sp),parameter :: x1=1.,x2=-1,y1=.23,y2=3.

call random_number(xmins)
call random_number(ymaxs)
call random_number(xmaxs)
call random_number(ymins)

call loop_cohensutherland(xmins,ymaxs,xmaxs,ymins,Np,x1,y1,x2,y2,length)


end function test_loop

logical function test_lineclip()

    use lineclip, only : sp,cohensutherland,assert,stdout

    real(sp) :: x1, y1, x2, y2 
    logical outside

!    make box with corners LL/UR (1,3) (4,5)
!    and line segment with ends (0,0) (4,6)

! LOWER to UPPER test   

    x1=0.; y1=0.; x2=4.; y2=6.;

    call cohensutherland(1., 5., 4., 3.,x1,y1,x2,y2,outside)
    
    call assert(abs(x1-2.).lt.1e-3)
    call assert(abs(y1-3.).lt.1e-3)
    call assert(abs(x2-3.3333333).lt.1e-3)
    call assert(abs(y2-5.).lt.1e-3)

    write(stdout,*) 'OK'

    test_lineclip=.true.

end function test_lineclip

end program
