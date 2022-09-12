/*
 * beforeafter
 *
 *   SYNOPSIS
 *
 *       beforeafter before_file after_file
 *
 *   Description
 *
 *       Sutract the numbers in before_file from the numbers in
 *       after_file.
 * 
 *   Example
 *
 *       > netstat -s > netstat.before
 *       > run some test here
 *	 > netstat -s > netstat.after
 *	 > beforeafter netstat.before netstat.after
 */

#include <stdio.h>
#include <ctype.h>

char	*USAGE = "before_file after_file";

main(argc, argv)
    int		argc;
    char	*argv[];
    
{
    FILE	*fp1;		/* "before" file */
    FILE	*fp2;		/* "after" file */
    char	*fname1;
    char	*fname2;
    int		c;
    int		c2;
    unsigned int	n1 = 0;
    unsigned int	n2 = 0;
    int		separator;
    int		separator2;
    
    /*
     * Checke # of arguments.
     */
    if (argc != 3)
    {
	fprintf(stderr, "Usage: %s %s\n", argv[0], USAGE);
	exit (1);
    }
    /*
     * Open files.
     */
    fname1 = argv[1];
    fname2 = argv[2];
    fp1 = fopen(fname1, "r");
    fp2 = fopen(fname2, "r");
    if (!fp1 || !fp2)
    {
	fprintf(stderr, "fp1 = 0X%x  fp2 = 0X%x", fp1, fp2);
	perror ("Could not open files");
	exit (2);
    }
    /*
     * Parse.
     */
    while ((c = getc(fp1)) != EOF)
    {
	if (c == ' ' || c == '\t' || c == ':' || c == '(')
	{
	    printf("%c", c);
	    separator = 1;
	}
	else if (!isdigit(c))
	{
	    printf("%c", c);
	    separator = 0;
	}
	else 
	{
	    if (separator == 0)
	    {
		printf("%c", c);	/* this digit is a part of a word */
		continue;
	    }
	    n1 = c - '0';
	    while ((c = getc(fp1)) != EOF)
	    {
		if (isdigit(c))
		{
		    n1 = 10 * n1 + c - '0';
		}
		else
		{
		    break;
		}
	    }
	    /*
	     * Find the counterpart in the "after" file.
	     */
	    while ((c2 = getc(fp2)) != EOF)
	    {
		if (c2 == ' ' || c2 == '\t' || c2 == ':' || c2 == '(')
		{
		    separator2 = 1;
		}
		else if (!isdigit(c2))
		{
		    separator2 = 0;
		}
		else
		{
		    if (separator2 == 0)
		    {
			continue;
		    }
		    n2 = c2 - '0';
		    while ((c2 = getc(fp2)) != EOF)
		    {
			if (isdigit(c2))
			{
			    n2 = 10 * n2 + c2 - '0';
			}
			else
			{
			    break;
			}
		    }
		    break;
		}
	    }
	    printf ("%u", n2 - n1);
	    if (c != EOF)
	    {
		printf("%c", c);
	    }
	}
    }
}

	
