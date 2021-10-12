package movierental;
/**
 * A rental of a movie by customer.
 * From Fowler's refactoring example.
 * 
 * Rental should have fields and methods for the dates
 * that the movie was rented and returned, from which the
 * rental period is calculated.
 * But for simplicity of the example only a daysRented
 * field is shown.
 */
public class Rental {
	private Movie movie;
	private int daysRented;

	
	/** Initialize a new movie rental object for
	 * a movie with known rental period (daysRented).
	 */
	public Rental(Movie movie, int daysRented) {
		this.movie = movie;
		this.daysRented = daysRented;
	}


	/**
	 * @return the movie
	 */
	public Movie getMovie() {
		return movie;
	}


	/**
	 * @return the daysRented
	 */
	public int getDaysRented() {
		return daysRented;
	}
	
	

}
