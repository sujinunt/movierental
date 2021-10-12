package movierental;

import static org.junit.Assert.*;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.junit.Before;
import org.junit.Test;

public class CustomerTest {

	/** A customer for use in tests. */
	Customer c;
	Movie [] movies;
	
	@Before
	public void setUp() throws Exception {
		c = new Customer("Movie Mogul");
		movies = new Movie[] {
				new Movie("CitizenFour", Movie.REGULAR),
				new Movie("Frozen", Movie.CHILDRENS),
				new Movie("Ex Machina", Movie.NEW_RELEASE),
				new Movie("Bridge of Spies", Movie.NEW_RELEASE),
				new Movie("Particle Fever", Movie.REGULAR)
		};
	}

	@Test
	public void testBilling() {
		// no convenient way to test billing since its buried in the statement() method.
	}
	
	@Test
	public void testStatement() {
		String stmt = c.statement();
		System.out.println(stmt);
		// a cludgy way of getting total charges from statement
		Pattern matchCharges = Pattern.compile(".*Total [Cc]harges.*(\\d+\\.\\d\\d).*");
		Matcher matcher = matchCharges.matcher(stmt);
		assertTrue("Statement doesn't contain Total charges string",matcher.matches());
		String amountstr = matcher.group(1);
		assertEquals("0.00", amountstr);
	}
	
	

}
